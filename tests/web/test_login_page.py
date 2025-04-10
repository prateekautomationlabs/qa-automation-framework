from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_invalid_login(page, config):
    page.goto(config['base_url'])
    home = HomePage(page)
    home.click_signup_login()

    login = LoginPage(page)
    login.login("fake@example.com", "wrongpass")
    assert login.is_error_displayed()

def test_empty_login_fields(page, config):
    page.goto(config['base_url'] + "/login")
    login = LoginPage(page)
    login.login("", "")
    assert login.is_error_displayed()
