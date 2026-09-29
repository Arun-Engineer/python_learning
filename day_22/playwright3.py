from playwright.sync_api import sync_playwright, expect

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel = "chrome", headless = False, slow_mo = 1000)
        page = browser.new_page()

        page.goto("https://example.com/login")

        page.get_by_label("Username").fill("sam")
        page.get_by_text("Password").fill("secret123")

        page.get_by_role("button", name= "Login").click()

        expect(page.get_by_text("Welcome, sam")).to_be_visible

        browser.close()
test_login_success()