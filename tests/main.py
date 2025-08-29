from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create a new page
    page = browser.new_page()
    # Visit the playwright website
    page.goto("https://bootswatch.com/default")

    #  Locate a link element with "Docs" text

    link = page.locator("a.dropdown-item").first
    link.click(timeout=2000) # force=True


    browser.close()