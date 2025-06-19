import pytest
from playwright.sync_api import sync_playwright, expect

URL = "https://practicetestautomation.com/practice-test-login/"

def test_positive_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(URL)
        page.fill('#username', 'student')
        page.fill('#password', 'Password123')
        page.click('#submit')

        # Verificaciones
        assert "/logged-in-successfully/" in page.url
        assert "Congratulations" in page.content() or "successfully logged in" in page.content()
        assert page.locator("text=Log out").is_visible()
        browser.close()

def test_invalid_username():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(URL)
        page.fill('#username', 'incorrectUser')
        page.fill('#password', 'Password123')
        page.click('#submit')

        expect(page.locator('#error')).to_have_text("Your username is invalid!")
        browser.close()

def test_invalid_password():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(URL)
        page.fill('#username', 'student')
        page.fill('#password', 'incorrectPassword')
        page.click('#submit')

        expect(page.locator('#error')).to_have_text("Your password is invalid!")
        browser.close()
