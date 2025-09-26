from playwright.sync_api import sync_playwright

def on_filechooser(file_chooser):
    print("File chooser opened:")
    file_chooser.set_files(r"tests\main.py")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=500
    )

    page = browser.new_page()
    page.on("filechooser", on_filechooser)

    page.goto("https://bootswatch.com/default")

    file_input = page.get_by_label("Default file input example")
    file_input.click()

    browser.close()