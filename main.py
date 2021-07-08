from playwright.sync_api import Page

url = 'https://www.google.com/'


def test_google_search_playwright(page: Page):
    page.goto(url)
    page.click("[aria-label=\"Search\"]")
    page.fill("[aria-label=\"Search\"]", "playwright")
    with page.expect_navigation():
        page.click("text=Google Search")
    assert page.is_visible("text=Playwright - Microsoft Edge Development | Microsoft Docs")
