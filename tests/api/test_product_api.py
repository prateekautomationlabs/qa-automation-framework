# tests/api/test_product_api.py

import pytest
from pages.api.product_api_page import ProductAPIPage

@pytest.fixture(scope="module")
def product_api(api_client):  # Using the fixture from conftest.py
    return ProductAPIPage(api_client)

def test_get_all_products(product_api):
    response = product_api.get_all_products()
    print("printing response json:", response.json())
    assert response.status_code == 200
    assert "products" in response.json()

def test_search_product_found(product_api):
    response = product_api.search_product("Tshirt")
    assert response.status_code == 200
    assert any("Tshirt" in p["name"] for p in response.json().get("products", []))

def test_search_product_not_found(product_api):
    response = product_api.search_product("xyznotfound")
    assert response.status_code == 200
    assert response.json().get("products") == []
