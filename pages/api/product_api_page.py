# pages/product_api_page.py

from api_clients.product_client import ProductClient

class ProductAPIPage:
    def __init__(self, session):
        self.client = ProductClient(session)

    def get_all_products(self):
        return self.client.get_all_products()

    def search_product(self, name: str):
        return self.client.search_product(name)
