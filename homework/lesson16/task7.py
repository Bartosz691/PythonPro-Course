def parse_url(url: str) -> dict:
    protocol, rest = url.split("://", 1)

    if "/" in rest:
        domain_port, path = rest.split("/", 1)
        path = "/" + path
    else:
        domain_port = rest
        path = "/"

    if ":" in domain_port:
        domain, port = domain_port.split(":", 1)
        port = int(port)
    else:
        domain = domain_port

        if protocol == "http":
            port = 80
        elif protocol == "https":
            port = 443
        else:
            port = None

    return {
        "protocol": protocol,
        "domain": domain,
        "port": port,
        "path": path
    }


if __name__ == "__main__":
    url = "https://api.example.com:8080/users/search?active=true"

    wynik = parse_url(url)

    print(wynik)