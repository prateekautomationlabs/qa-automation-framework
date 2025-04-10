from pages.base_page import BasePage

class SignupPage(BasePage):
    name_input = "input[data-qa='signup-name']"
    email_input = "input[data-qa='signup-email']"
    signup_button = "button[data-qa='signup-button']"
    error_msg = "p"

    def signup(self, name, email):
        self.page.fill(self.name_input, name)
        self.page.fill(self.email_input, email)
        self.page.click(self.signup_button)

    def is_error_displayed(self):
        return self.page.is_visible(self.error_msg)
