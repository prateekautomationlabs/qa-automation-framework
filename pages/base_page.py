

class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, text):
        self.page.fill(locator, text)

    def is_visible(self, locator):
        return self.page.is_visible(locator)

    def get_text(self, locator):
        return self.page.inner_text(locator)