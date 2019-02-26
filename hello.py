def app(environ, start_response):
    data = [bytes(item+'\n','ascii') for item in environ['QUERY_STRING'].split('&')]
    start_response("200 OK", [
        ("Content-Type", "text/plain")
    ])
    return data
