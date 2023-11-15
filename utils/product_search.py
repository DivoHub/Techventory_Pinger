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

class SeleniumDriver(Driver):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selenium_path = pathlib.Path('selenium').resolve()
        self.selenium_path.mkdir(exist_ok=True)
        self.driver_path = self.selenium_path / 'chromedriver'
        driver_paths = [
            '/usr/bin/chromedriver',
            '/usr/local/bin/chromedriver',
        ]
        for driver_path in driver_paths:
            if os.path.exists(driver_path):
                # chromedriver needs to be patched to avoid detection, see:
                # https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver
                shutil.copy(driver_path, self.driver_path)
                with open(driver_path, 'rb') as f:
                    variables = set([m.decode('ascii') for m in re.findall(b'cdc_[^\' ]+', f.read())])
                    for v in variables:
                        replacement = ''.join(random.choice(string.ascii_letters) for i in range(len(v)))
                        logging.debug(f'found variable in chromedriver: {v}, replacing with {replacement}')
                        cmd = ['perl', '-pi', '-e', f's/{v}/{replacement}/g', self.driver_path]
                        r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, text=True)
                        if r.returncode != 0:
                            logging.warning(f'chromedriver patch failed: {r.stdout}')
                break

        if not self.driver_path.is_file():
            raise Exception(f'Selenium Chrome driver not found at {" or ".join(driver_paths)}')

        self.options = webdriver.ChromeOptions()
        self.options.page_load_strategy = 'eager'
        if getpass.getuser() == 'root':
            self.options.add_argument('--no-sandbox')  # required if root
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument(f'--user-agent="{user_agent}"')
        self.options.add_argument(f'--user-data-dir={self.selenium_path}')
        self.options.add_argument('--window-position=0,0')
        self.options.add_argument('--window-size=1920,1080')
