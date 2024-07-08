import self

from swagger_client.api import DefaultApi

if __name__ == "__main__":
    loginAPI = DefaultApi()
    login_body = {
        "userId": "DBG101",
        "password": "Akshaya@12",
        "mobileNumber": "7305989193"
    }
    appId = "test"
    response_body, status_code, headers = loginAPI.login_normal_login_post(login_body, appId)
    print("response: " + str(response_body))

    # access_token = response_body.data.accessToken

    # print("accessToken: " + str(access_token))
