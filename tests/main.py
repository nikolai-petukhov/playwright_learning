from playwright.sync_api import sync_playwright
from creds import EMAIL, PASSWORD


with sync_playwright() as playwright:
    
    browser = playwright.firefox.launch(headless=False, slow_mo=500) #args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"]
    context = browser.new_context()
    
    page = context.new_page()
    
    page.goto("https://www.21vek.by")


    accept_coockies = page.get_by_role("button", name="Принять")
    account_button = page.get_by_text("Аккаунт")
    enter_button = page.get_by_role("button", name="Войти")
    email_input = page.get_by_label("Электронная почта")
    password_input = page.get_by_label("Пароль")
    continue_button = page.get_by_role("button", name="Продолжить")

    accept_coockies.click()
    account_button.click()
    enter_button.click()
    email_input.fill(EMAIL)
    password_input.fill(PASSWORD)
    continue_button.click()

    page.pause()

    context.storage_state(
        path="playwright/.auth/storage_state.json"
    )

    context.close()