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
        """Navigate to the Contact Us page."""
        self.click(self.contact_btn)

    def submit_form(self, name, email, subject, message):
        """Fill out and submit the contact form."""
        self.fill(self.name_input, name)
        self.fill(self.email_input, email)
        self.fill(self.subject_input, subject)
        self.fill(self.message_input, message)
        self.scroll_into_view(self.submit_btn)
        self.click(self.submit_btn)
        # Handle any dialog that appears after submission
        self.page.once("dialog", lambda dialog: dialog.accept())

    def is_success_displayed(self):
        """Check if the success message is displayed."""
        return self.is_visible(self.success_msg)