from playwright.sync_api import Page, expect
import pytest

#runs before each function
@pytest.fixture(autouse=True, scope="function")
def go_to_page(page:Page):
   page.goto("https://playwright.dev/python")
   yield page
   page.close()
   

def test_page_has_get_started_link(page:Page):
    get_started = page.get_by_role("link",name="Get started")
    # get_started_visibility = get_started.is_visible()
    # assert get_started_visibility == True
    expect(get_started).to_be_visible()