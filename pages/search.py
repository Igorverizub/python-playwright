class SearchPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto('https://www.google.com/')

    def search(self, text):
        self.page.fill('[aria-label=\"Search\"]', text)
        self.page.press('[aria-label=\"Search\"]', "Enter")
