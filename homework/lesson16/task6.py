from dataclasses import dataclass, field
from enum import StrEnum, auto

class HttpMEthod(StrEnum):
    GET = auto() # 'get'
    POST = auto() # 'post'
    PUT = auto()
    PATCH = auto()
    
@dataclass
class HttpRequest:
    method: HttpMEthod
    target: str
    headers: dict = field(default_factory=dict)
    body: dict = field(default_factory = dict)
    
def __post_init__(self):
    if not isinstance(self.metod, HttpMEthod):
        raise TypeError("Wrong type of method attr.")
    
def display(self):
    print(f"""---HTTP Request ---
     Method: {self.method}     
      Target: {self.target}
      Headers:
      Host: example.compile
      User-Agent: {self.headers.get('user-agent', '<empty')}    
       Body:
       (empty)   
      -----------------------    """)
    
HttpRequest()