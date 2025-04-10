from pages.base_page import BasePage

class ContactUsPage(BasePage):
    contact_btn = "a[href='/contact_us']"
    name_input = "[name='name']"
    email_input = "[name='email']"
    subject_input = "[name='subject']"
    message_input = "#message"
    submit_btn = "[name='submit']"
    success_msg = ".status.alert-success"

    def navigate_to_contact(self):
        self.page.click(self.contact_btn)

    def submit_form(self, name, email, subject, message):
        self.page.fill(self.name_input, name)
        self.page.fill(self.email_input, email)
        self.page.fill(self.subject_input, subject)
        self.page.fill(self.message_input, message)
        self.page.click(self.submit_btn)

    def is_success_displayed(self):
        return self.page.is_visible(self.success_msg)
