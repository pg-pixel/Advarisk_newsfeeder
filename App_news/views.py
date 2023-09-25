"""
This file is the view file of the app App_news.
This contains class based views required to handle appropriate request
"""
# import django libraries
from django.shortcuts import render, HttpResponse, redirect
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator, EmptyPage
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

# import custom packages
from .Logic.api import Logic_run, Api_helper
from App_news.forms import SearchHistoryForm
from .models import SearchHistory 
from App_user.models import CustomUser 

# Create your views here.
class Index(View):
    """ 
    This is the starting view of the application
    """
    def get(self, request):
        """ 
        This method renders a template. The template is the Index of the Application.
        """
        return render(request, 'App_news/index.html', {})
         
@method_decorator(login_required, name='dispatch') 
class News(View):
    """ 
    This class is handling CRUD operations for showing searched request.
    """
    def get_cache_key(self, request):
        """
        This function will overwrite existing django cache key creation so that we can ignore user information in the request.
        """
        cacheable_query_params = {}
        
        cacheable_query_params['search_query'] = request.POST.get('Search_parameter')
        cacheable_query_params['from_date'] = request.POST.get('since')
        
        cache_key = 'query_params:' + '&'.join([f"{key}={value}" for key, value in cacheable_query_params.items()])

        return cache_key
        
    def check_limit(self, request_dto):
        """
        This method returns a boolean value if user is has exceeded his/her dailylimit or not.
        """
        now = timezone.now()
        start_of_day = timezone.make_aware(timezone.datetime(now.year, now.month, now.day))
        end_of_day = start_of_day + timezone.timedelta(days=1)
        
        curr_used = SearchHistory.objects.filter(Manager = request_dto._user,
                                                 time_stamp__range = (start_of_day, end_of_day)).count() 
        
        user_limit = CustomUser.objects.filter(username = request_dto._user).values('daily_request_limit')
        
        return user_limit[0]['daily_request_limit'] > curr_used
            
    def get(self, request):
        """ 
        This method returns empty data 
        """
        
        query_set = CustomUser.objects.filter(username = request.user).values('is_blocked')
        
        if query_set[0]['is_blocked']:
            context = {'msg':'Please contact admin activate your access.'}
            return render(request, 'App_news/Access_NA.html', context)
        
        context ={'query':None, 'data':[]}
        
        return render(request,'App_news/home.html' ,context) 
    
    
    def post(self, request):
        """ 
        This method returns news article.
        """
        print('hitting request')
        print('##')
        form = SearchHistoryForm(request.POST or None) # instance of the form 
        if form.is_valid():
            _request_dto = Api_helper.get_request_dto(request) # create request dto 
            if self.check_limit(_request_dto):
            
                # create a query set to fetch if search parameter already exist or not for the user
                query_set = SearchHistory.objects.filter(Search_parameter=_request_dto._query, Manager=_request_dto._user).first()
                
                if not query_set:# if first time searching
                    form.instance.Manager = _request_dto._user
                    form.save()
                else:# updating time stamp
                    query_set.save()
                
                # fetching result
                _result = Logic_run()
                _data = _result(_request_dto) 
                
                context = {'query':_request_dto, 'data': _data['Articles']}
                
                return render(request,'App_news/home.html' ,context)
            else: # limit reached 
                context = {'msg': 'Daily Limit reached.'}
                return render(request, 'App_news/Access_NA.html', context)
        
        return redirect('Homepage')
     
@method_decorator(login_required, name='dispatch')    
class History(View):
    """
    This class is handling views related to search query
    """
    def get(self, request):
        """
        This method will fetch searched parameter for a particular user 
        """
        query_set = SearchHistory.objects.filter(Manager=request.user)
        
        if not query_set:
            context = {'history': ['No searches Made']} 
        else:
            context = {'history': query_set} 
            
        return render( request, 'App_news/history.html', context)
        