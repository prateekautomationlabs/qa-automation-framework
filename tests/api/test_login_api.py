# tests/api/test_login_api.py

from pages.api.login_api_page import LoginAPIPage

def test_verify_login_valid_user(api_client):
    login_page = LoginAPIPage(api_client)
    response = login_page.verify_login_success("prateekautomationlabs@gmail.com", "Test@123")
    print(response.text)
    assert response.status_code == 200
    assert "User exists!" in response.text
