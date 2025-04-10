from pages.base_page import BasePage

class LoginPage(BasePage):
    email_input = "input[data-qa='login-email']"
    password_input = "input[data-qa='login-password']"
    login_button = "button[data-qa='login-button']"
    error_msg = "p"

    def login(self, email, password):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_error_displayed(self):
        return self.page.is_visible(self.error_msg)
