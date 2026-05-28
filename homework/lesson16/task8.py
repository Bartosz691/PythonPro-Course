
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any

class HTTP_METHODS(Enum):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    
@dataclass
class HttpResp:
    code: int
    data: dict

class FakeServer:
    
    def __init__(self):
        self.db = {"users": [{"id1": 1, "name": "Jan"},
                            {"id": 2, "name": "Anna"} ]}
        
    def handle_request(self, request: dict):
        """{'method': GET | POST | PUT | DELETE',
        
        }
        """
        
        method = request['method']
        if request['method'] == HTTP_METHODS.GET:
            return self._get(request)
        elif method  == HTTP_METHODS.POST: 
         ...
         
    def _get(self, request: dict):
        # GET server/users -> wszystkich użytkowników
        p: str = request['path'] 
        if p == '/users':
           return HttpResp(200, {'users': self.db['users']})
        #GET server/users/{id} -> zwracamy konkretnego użytkownika
        if p.startswith('/users/'):
           try: 
             return self._db_user_by_id(int(p.rsplit('/',1)))
           except   ValueError:
                return HttpResp(200, user)
           except StopIteration:
               ...
    def _db_user_by_id(self, id: int):
        for user in self.db['users']:
            if user['id'] == id:
                return user
        raise StopIteration        