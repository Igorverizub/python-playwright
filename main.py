from playwright.sync_api import Page
import pytest


@pytest.mark.only_browser("chromium")
def test_test(page: Page):
    url = 'https://aws.amazon.com/'
    page.goto(url)
    assert page.url == url


@pytest.mark.only_browser("chromium")
def test_test2(page: Page):
    url = 'https://aws.amazon.com/'
    page.goto(url)
    assert page.url == url


@pytest.mark.only_browser("chromium")
def test_test3(page: Page):
    url = 'https://aws.amazon.com/'
    page.goto(url)
    assert page.url == url


@pytest.mark.only_browser("chromium")
def test_test4(page: Page):
    url = 'https://aws.amazon.com/'
    page.goto(url)
    assert page.url == url


@pytest.mark.only_browser("chromium")
def test_test5(page: Page):
    url = 'https://aws.amazon.com/'
    page.goto(url)
    assert page.url == url
