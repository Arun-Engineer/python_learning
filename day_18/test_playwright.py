from playwright.sync_api import sync_playwright

# def test_example():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()

#         page.goto("https://example.com")

#         title = page.title()
#         assert "Example" in title

#         browser.close()

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel = "chrome", headless = False, slow_mo = 1000)
        page = browser.new_page()
        page.goto("https://example.com")
        print("Page title: ", page.title())
        assert "Example" in page.title()
        page.wait_for_timeout(3000)
        browser.close() 

test_example()