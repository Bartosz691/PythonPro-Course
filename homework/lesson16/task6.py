from dataclasses import dataclass, field
from enum import StrEnum, auto


class HttpMethod(StrEnum):
    GET = auto()
    POST = auto()
    PUT = auto()
    PATCH = auto()


@dataclass
class HttpRequest:
    method: HttpMethod
    target: str
    headers: dict = field(default_factory=dict)
    body: str = ""

    def __post_init__(self):
        if not isinstance(self.method, HttpMethod):
            raise TypeError("Wrong type of method attr.")

    def display(self):
        print("--- HTTP Request ---")
        print(f"Method: {self.method}")
        print(f"Target: {self.target}")

        print("Headers:")
        if self.headers:
            for key, value in self.headers.items():
                print(f"{key}: {value}")
        else:
            print("(empty)")

        print("Body:")
        if self.body:
            print(self.body)
        else:
            print("(empty)")

        print("--------------------")


# Test wymagany w zadaniu
request = HttpRequest(
    method=HttpMethod.POST,
    target="/api/users",
    headers={
        "Host": "example.com",
        "User-Agent": "PythonClient/1.0",
        "Content-Type": "application/json"
    },
    body='{"name": "Jan", "age": 25}'
)

request.display()