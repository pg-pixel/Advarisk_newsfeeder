"""
This file is the client implementation of the API used for the Assessment
"""
# import #rd party libraries
from newsapi import NewsApiClient 

# import other libraries
from datetime import datetime 
from django.conf import settings

class Api_client:
    """
    This class is responsible for creating newsapi and fetch its result
    """
    def __call__(self, search, _to, from_date, _sort_by, _language ):
        """
        This method will use api to fetch result
        """
        return self.get_api_result(search, from_date, _sort_by, _language, _to)
    
    def __init__(self):
        """
        Creates a newsapi client object
        """
        #api_key='48e8f9ae3b584252bd46d8e7b41631f9'
        self.newsapi = NewsApiClient(api_key=f'{settings.API_KEY}') 
        
    def get_api_result(self, search, from_date, _sort_by, _language, _to):
        """
        This method is responsible for sending request. It internally uses get_everything method of the API.
        Kindly refer documentation of the API.
        """
        return self.newsapi.get_everything(q=search,
                                           from_param = from_date,
                                           to = _to,
                                           language = _language,
                                           sort_by = _sort_by
                                           )
        
if __name__ == '__main__':
    obj = Api_client()
    curr = datetime.now()
    _to = curr.strftime("%Y-%m-%dT%H:%M:%S")
    print(obj('srk', _to, from_date = None, _sort_by = 'publishedAt', _language = 'en'))

    