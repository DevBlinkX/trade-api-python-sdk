import self

from swagger_client.api import DefaultApi

if __name__ == "__main__":
    loginAPI = DefaultApi
    login_body = {
        "userId": "DBG101",
        "password": "Akshaya@12",
        "mobileNumber": "7305989193"
    }
    appId = "test"
    loginAPI.login_normal_login_post(DefaultApi, login_body, appId)
