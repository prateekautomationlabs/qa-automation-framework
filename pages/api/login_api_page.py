# pages/login_api_page.py
from api_clients.login_client import LoginAPI_Client

class LoginAPIPage:
    def __init__(self, api_client):
        self.api = LoginAPI_Client(api_client)

    def verify_login_success(self, email, password):
        response = self.api.verify_login(email, password)
        assert response.status_code == 200
        assert response.json()["message"] == "User exists!"
        return response
