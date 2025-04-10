from pages.products_page import ProductsPage
from pages.home_page import HomePage

def test_product_search_found(page, config):
    page.goto(config['base_url'])
    home = HomePage(page)
    home.go_to_products()

    products = ProductsPage(page)
    products.search_product("Dress")
    assert products.get_number_of_products() > 0

def test_product_search_not_found(page, config):
    page.goto(config['base_url'] + "/products")
    products = ProductsPage(page)
    products.search_product("NoSuchItem")
    assert products.get_number_of_products() == 0
