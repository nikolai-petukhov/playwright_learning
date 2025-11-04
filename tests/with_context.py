from playwright.sync_api import sync_playwright
from creds import EMAIL, PASSWORD


with sync_playwright() as playwright:
    
    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        storage_state="playwright/.auth/storage_state.json"
    )
    
    page = context.new_page()
    
    page.goto("https://www.21vek.by")


    page.pause()

    context.close()