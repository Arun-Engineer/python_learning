from playwright.sync_api import sync_playwright, expect

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel = "chrome", headless = False, slow_mo = 1000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")

        success_message = page.locator(".flash.success")
        expect(success_message).to_be_visible()
        expect(success_message).to_contain_text("logged into")

        print("Login test passed - success message visible")
        page.click(".icon-2x.icon-signout")
        logut_mesage = page.locator(".flash.success")
        expect(logut_mesage).to_be_visible()
        expect(logut_mesage).to_contain_text("logged out")
        print("Logout test passed - success message visible")
        browser.close()

test_login_success()

def login_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel= "chrome", headless= False, slow_mo= 1000)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")

        page.fill("#username", "wronguser")
        page.fill("#password", "wrongpass")
        page.click("button[type='submit']")
        expect(page.locator(".flash.error")).to_be_visible()

        browser.close()

login_fail()