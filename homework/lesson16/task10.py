def validate_request(request_dict: dict):
    headers = request_dict.get("headers", {})

    if "Host" not in headers:
        raise ValueError("Brak wymaganego nagłówka: Host")

    if "User-Agent" not in headers:
        raise ValueError("Brak wymaganego nagłówka: User-Agent")

    return True


poprawne_zadanie = {
    "method": "GET",
    "target": "/index.html",
    "headers": {
        "Host": "example.com",
        "User-Agent": "PythonClient/1.0"
    }
}

niepoprawne_zadanie = {
    "method": "GET",
    "target": "/index.html",
    "headers": {
        "Host": "example.com"
    }
}

try:
    validate_request(poprawne_zadanie)
    print("Poprawne żądanie.")
except ValueError as e:
    print(e)

try:
    validate_request(niepoprawne_zadanie)
    print("Poprawne żądanie.")
except ValueError as e:
    print(e)