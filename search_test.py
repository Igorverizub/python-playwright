from playwright.sync_api import Page
from pages.search import SearchPage

url = 'https://www.google.com/'


def test_google_search_playwright(page: Page):
    page.goto(url)
    page.click("[aria-label=\"Search\"]")
    page.fill("[aria-label=\"Search\"]", "playwright")
    with page.expect_navigation():
        page.click("text=Google Search")
    page.click("text=microsoft/playwright: Node.js library to automate ... - GitHub")
    assert page.url == "https://github.com/microsoft/playwright"


def test_search(page: Page):
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("playwright")
    assert 'playwright' in page.url
