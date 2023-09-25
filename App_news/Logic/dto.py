"""
This is the file conatining dto implementation
"""

from datetime import datetime 

class Request_dto:
    """
    request dto class
    """
    def __init__(self):
        self._query = None
        self._to = datetime.now().strftime("%Y-%m-%dT%H:%M:%S") 
        self.since  = None 
        self._sort_by = 'publishedAt'
        self._language = 'en'
        self._user = None
        
    @property
    def query(self):
        return self._query 
    
    @property
    def to(self):
        return self._to
        
   
        
class Api_response_dto:
    """
    Api response dto class
    """
    def __init__(self):
        self.author = None
        self.title = None
        self.description = None
        self.url = None
        self.urlToImage = None
        self.publishedAt = None
        self.content = None

        