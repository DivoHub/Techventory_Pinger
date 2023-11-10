import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4427.0 Safari/537.36'


def bing_query(query):

    url = f"https://www.bing.com/shop?q={query.replace(' ', '+')}"
    request = requests.get(url)
    request = BeautifulSoup(request.text, "html.parser")
    request.find_all("li", class_="br-item")

class HttpGetResponse:
    def __init__(self, text, url, **kwargs):
        self.text = text
        self.url = url
        self.status_code = kwargs.get('status_code', None)

class RequestsDriver(Driver):
    def get(self, url) -> HttpGetResponse:
        headers = {'user-agent': user_agent, 'referer': 'https://google.com'}
        r = requests.get(str(url), headers=headers, timeout=self.timeout)
        if not r.ok:
            print ("http error")
        return HttpGetResponse(r.text, r.url, status_code=r.status_code)
