from playwright.sync_api import sync_playwright, Page, expect
import pytest

@pytest.fixture
def page():
   playwright = sync_playwright().start()
   browser = playwright.chromium.launch(headless=False)
   return browser.new_page()
   

def test_page_has_get_started_link(page:Page):
    page.goto("https://playwright.dev/python")
    get_started = page.get_by_role("link",name="Get started")
    get_started_visibility = get_started.is_visible()
    assert  get_started_visibility == True