import requests


class Test:
    def test_ex12(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        print(response.headers)
        headers = response.headers
        exp_headers = "x-secret-homework-header"
        exp_headers_value = "Some secret value"
        assert exp_headers in headers, "Doesn't match headers"
        assert exp_headers_value in headers[exp_headers], "Doesn't match headers value"
