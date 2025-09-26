from playwright.sync_api import sync_playwright
from time import perf_counter


with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create a new page
    page = browser.new_page()

    # print("Page loading...")
    # start = perf_counter()

    # Visit the playwright website
    page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")

    link = page.get_by_role("link", name="2015")
    link.click()

    print("... loading oscars for 2015 ...")
    start = perf_counter()

    page.wait_for_selector(selector="td.film-title")

    time_taken = perf_counter() - start
    print(f"...movies are loaded, in {round(time_taken, 2)}!")

    # time_taken = perf_counter() - start
    # print(f"... page loaded in {round(time_taken, 2)}s")

    browser.close()