from pages.contact_us_page import ContactUsPage

def test_submit_contact_form(page, config):
    page.goto(config['base_url'])
    contact = ContactUsPage(page)
    contact.navigate_to_contact()
    contact.submit_form("User", "user@mail.com", "Test Subject", "Hello!")
    assert contact.is_success_displayed()

def test_submit_contact_form_blank_fields(page, config):
    page.goto(config['base_url'] + "/contact_us")
    contact = ContactUsPage(page)
    contact.submit_form("", "", "", "")
    assert not contact.is_success_displayed()
