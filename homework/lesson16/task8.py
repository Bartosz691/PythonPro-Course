from dataclasses import dataclass
from enum import Enum, IntEnum, auto


class HTTP_METHODS(Enum):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()


class HTTP_CODES(IntEnum):
    OK = 200
    CREATED = 201
    NOT_FOUND = 404


@dataclass
class HttpResp:
    code: int
    data: dict


class FakeServer:

    def __init__(self):
        self.__next_id = 3
        self.db = {
            "users": [
                {"id": 1, "name": "Jan"},
                {"id": 2, "name": "Anna"}
            ]
        }

    def handle_request(self, request: dict):
        method = request.get("method")
        path = request.get("path")

        if method == HTTP_METHODS.GET and path == "/users":
            return HttpResp(
                HTTP_CODES.OK,
                {"users": self.db["users"]}
            )

        elif method == HTTP_METHODS.POST and path == "/users":
            name = request.get("data", {}).get("name")

            if not name:
                return HttpResp(
                    HTTP_CODES.NOT_FOUND,
                    {"error": "Brak pola name"}
                )

            new_user = self.__db_user_create(name)

            return HttpResp(
                HTTP_CODES.CREATED,
                new_user
            )

        else:
            return HttpResp(
                HTTP_CODES.NOT_FOUND,
                {"error": "Not Found"}
            )

    def __db_user_create(self, name: str):
        new_user = {
            "id": self.__next_id,
            "name": name
        }

        self.db["users"].append(new_user)
        self.__next_id += 1

        return new_user


class FakeClient:

    def send(self, server: FakeServer, request: dict):
        print("\n--- Request ---")
        print(request)

        response = server.handle_request(request)

        print("--- Response ---")
        print(f"Code: {response.code}")
        print(f"Data: {response.data}")
        print("----------------")


if __name__ == "__main__":
    server = FakeServer()
    client = FakeClient()

  
    client.send(server, {
        "method": HTTP_METHODS.GET,
        "path": "/users"
    })


    client.send(server, {
        "method": HTTP_METHODS.POST,
        "path": "/users",
        "data": {"name": "Piotr"}
    })


    client.send(server, {
        "method": HTTP_METHODS.GET,
        "path": "/users"
    })


    client.send(server, {
        "method": HTTP_METHODS.GET,
        "path": "/products"
    })