from pages.home_page import HomePage

def test_logo_visible(page, config):
    page.goto(config['base_url'])
    home = HomePage(page)
    assert home.is_logo_displayed()

def test_navigate_to_products(page, config):
    page.goto(config['base_url'])
    home = HomePage(page)
    home.go_to_products()
    assert "products" in page.url
