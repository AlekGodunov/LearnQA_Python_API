import requests
import pytest

class Test:

    userAgent = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize('userAgent', userAgent)
    def test_user_agent(self, userAgent):

        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"

        device = [
            ("Android"),
            ("iOS"),
            ("Unknown"),
            ("No"),
            ("iPhone")
        ]
        browser = [
            ("No"),
            ("Chrome"),
            ("Unknown")
        ]
        platform = [
            ("Mobile"),
            ("Googlebot"),
            ("Web")
        ]

        response = requests.get(url, headers={"User-Agent": userAgent})
        response_browser = response.json()["browser"]
        response_device = response.json()["device"]
        response_platform = response.json()["platform"]

        if userAgent == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
            assert response_browser == browser[0], f"This browser is not equal {browser[0]}"
            assert response_device == device[0], f"This device is not equal {device[0]}"
            assert response_platform == platform[0], f"This platform is not equal {platform[0]}"


        elif userAgent == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
            assert response_browser == browser[1], f"This browser is not equal {browser[1]}"
            assert response_device == device[1], f"This device is not equal {device[1]}"
            assert response_platform == platform[0], f"This platform is not equal {platform[0]}"

        elif userAgent == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
            assert response_browser == browser[2], f"This browser is not equal {browser[2]}"
            assert response_device == device[2], f"This device is not equal {device[2]}"
            assert response_platform == platform[1], f"This platform is not equal {platform[1]}"

        elif userAgent == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
            assert response_browser == browser[1], f"This browser is not equal {browser[1]}"
            assert response_device == device[3], f"This device is not equal {device[3]}"
            assert response_platform == platform[2], f"This platform is not equal {platform[2]}"

        elif userAgent == "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1":
            assert response_browser == browser[0], f"This browser is not equal {browser[0]}"
            assert response_device == device[4], f"This device is not equal {device[4]}"
            assert response_platform == platform[0], f"This platform is not equal {platform[0]}"

    