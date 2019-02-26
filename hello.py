def app(environ, start_response):
    data = [item+'\n' for item in environ['QUERY_STRING'].split('&')]
    start_response("200 OK", [
        ("Content-Type", "text/plain")
    ])
    return data
