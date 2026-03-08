import pytest
from playwright.sync_api import Browser, Page

DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture
def recordable_page(browser: Browser):
    context = browser.new_context(
        record_video_dir="./videos",
    )
    page = context.new_page()
    yield page
    context.close()


def test_page_has_get_started_link(recordable_page: Page) -> None:
    # Arrange
    page = recordable_page
    link_get_started = page.get_by_role("link", name="GET STARTED")
    # Act
    page.goto("https://playwright.dev/python/")
    page.screenshot(path="./screenshots/screenshot.png")
    link_get_started.click()
    page.wait_for_load_state("networkidle")
    page.screenshot(path="./screenshots/docs.png")
    # Assert
    assert page.url == DOCS_URL