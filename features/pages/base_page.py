class BasePage:
    def __init__(self, browser, url, timeout=7):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)
