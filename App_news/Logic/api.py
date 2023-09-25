"""
This is main file of the Logic directory.
This file helps in creating response and request dto.
This file helps in calling 3rd party API 
"""
# import python libraries
from datetime import datetime

# import custom package
from .api_client import Api_client
from .dto import Request_dto, Api_response_dto


class Api_helper:
    """
    This class is responsible for creating dto and fetching data
    """
    
    @staticmethod 
    def get_request_dto(request):
        """
        This method creates request dto
        """
        request_dto = Request_dto()
        request_dto._query = '+'.join(request.POST.get('Search_parameter').strip().split(' '))
        request_dto._user = request.user 
        request_dto.since = request.POST.get('since')
        
        return request_dto 
    
    @staticmethod 
    def get_news(api_result):
        """
        This method creates response map. 
        Map contains total result and a list of articles dto
        """
        _response_map = {'Total':api_result['totalResults']}
        _result = []
        for article in api_result['articles']:
            news_dto = Api_response_dto()
            news_dto.author = article.get('author')
            news_dto.title = article.get('title')
            news_dto.description = article.get('description')
            news_dto.url = article.get('url')
            news_dto.urlToImage = article.get('urlToImage')
            news_dto.publishedAt = article.get('publishedAt')
            news_dto.content = article.get('content')
            
            _result.append(news_dto) 
            
        _response_map['Articles'] = _result
            
        return _response_map
            
    @staticmethod 
    def get_data(request_dto):
        """
        This method calls API
        """
        _news =  Api_client()
        return _news(request_dto._query, request_dto._to, request_dto.since,
                    request_dto._sort_by, request_dto._language)
    
    
class Logic_run:
    """
    Orchestrator of the Logic directory
    """
    def __call__(self, request_dto):
        """
        This method returns response.
        Response is a map. It contains article count and a list of article dto
        """
        _data = Api_helper.get_data(request_dto) 
        _news_dto = Api_helper.get_news(_data)
        
        return _news_dto
        
        
        
    
    