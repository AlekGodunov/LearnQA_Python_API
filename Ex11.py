import requests


class Test:
    def test_ex11(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        print(response.cookies)
        cookies = response.cookies
        exp_cookies = "HomeWork"
        exp_cookies_value = "hw_value"
        assert exp_cookies in cookies, "Doesn't match cookies"
        assert exp_cookies_value in cookies["HomeWork"], "Doesn't match cookies value"

