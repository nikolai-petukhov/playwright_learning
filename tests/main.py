from playwright.sync_api import sync_playwright
from creds import EMAIL, PASSWORD


with sync_playwright() as playwright:
    
    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    
    page = browser.new_page()
    
    page.goto("https://accounts.google.com")

    email_input = page.get_by_label("Email or phone")
    next_button = page.get_by_role("button", name="Next")
    try_again_button = page.get_by_role("link", name="Try again")
    password_input = page.get_by_label("Enter your password")


    while True:
        email_input.fill(EMAIL)
        next_button.click()

        if try_again_button:
            try_again_button.click()
        else:
            break
    
    next_button.click()
    password_input.fill(PASSWORD)
    next_button.click()