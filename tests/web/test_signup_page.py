from pages.signup_page import SignupPage

def test_signup_with_existing_email(page, config):
    page.goto(config['base_url'] + "/login")
    signup = SignupPage(page)
    signup.signup("Test", "test@example.com")
    assert signup.is_error_displayed()

def test_signup_with_blank_fields(page, config):
    page.goto(config['base_url'] + "/login")
    signup = SignupPage(page)
    signup.signup("", "")
    assert signup.is_error_displayed()
