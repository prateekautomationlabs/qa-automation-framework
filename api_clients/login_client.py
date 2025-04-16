# api_clients/login_client.py

class LoginAPI_Client:
    def __init__(self, session):
        self.session = session
        self.endpoint = session.base_url + "verifyLogin"

    def verify_login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        return self.session.post(self.endpoint, data=payload)
