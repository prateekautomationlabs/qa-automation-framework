from pages.base_page import BasePage

class ProductsPage(BasePage):
    search_box = "#search_product"
    search_button = "#submit_search"
    product_list = ".features_items .product-image-wrapper"

    def search_product(self, product_name):
        self.page.fill(self.search_box, product_name)
        self.page.click(self.search_button)

    def get_number_of_products(self):
        return len(self.page.query_selector_all(self.product_list))
