from playwright.sync_api import sync_playwright

def test_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel = "chrome", headless = False, slow_mo = 1000)
        page = browser.new_page()

        page.goto("https://duckduckgo.com")

        page.fill("textarea[name ='q']", "Playwright testing")
        page.keyboard.press("Enter")

        page.wait_for_timeout(3000)
        print("Search done, title:", page.title)

        browser.close()

test_search()