from pages.base_page import BasePage

class HomePage(BasePage):
    logo = "img[alt='Website for automation practice']"
    signup_login_btn = "a[href='/login']"
    products_btn = "a[href='/products']"

    def is_logo_displayed(self):
        return self.page.is_visible(self.logo)

    def click_signup_login(self):
        self.page.click(self.signup_login_btn)

    def go_to_products(self):
        self.page.click(self.products_btn)
