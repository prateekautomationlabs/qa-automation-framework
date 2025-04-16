class ProductClient:
    def __init__(self, session):
        self.session = session  # requests.Session with base_url attached

    def get_all_products(self):
        return self.session.get(f"{self.session.base_url}productsList")

    def search_product(self, name: str):
        return self.session.post(
            f"{self.session.base_url}searchProduct",
            data={"search_product": name}
        )