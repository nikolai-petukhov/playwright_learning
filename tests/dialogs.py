from playwright.sync_api import sync_playwright

def on_dialog(dialog):
    print("dialog opened:", dialog)
    # dialog.dismiss()
    dialog.accept("lol")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=500
    )

    page = browser.new_page()

    page.goto("https://testpages.eviltester.com/styled/alerts/alert-test.html")

    page.on("dialog", on_dialog)

    alert_btn = page.get_by_text("Show prompt box")
    alert_btn.click()

    browser.close()