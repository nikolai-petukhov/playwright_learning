from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"

def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python/")
    page.screenshot(path="./screenshot.png")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    page.wait_for_load_state("networkidle")
    page.screenshot(path="./docs.png")

    assert page.url == DOCS_URL