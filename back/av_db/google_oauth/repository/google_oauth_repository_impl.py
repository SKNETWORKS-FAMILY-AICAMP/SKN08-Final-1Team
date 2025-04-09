import requests

from av_db import settings
from google_oauth.repository.google_oauth_repository import GoogleOauthRepository


class GoogleOauthRepositoryImpl(GoogleOauthRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.loginUrl = settings.GOOGLE['LOGIN_URL']
            cls.__instance.clientId = settings.GOOGLE['CLIENT_ID']
            cls.__instance.clientSecret = settings.GOOGLE['CLIENT_SECRET']
            cls.__instance.redirectUri = settings.GOOGLE['REDIRECT_URI']
            cls.__instance.tokenRequestUri = settings.GOOGLE['TOKEN_REQUEST_URI']
            cls.__instance.userInfoRequestUri = settings.GOOGLE['USER_INFO_REQUEST_URI']
            cls.__instance.revokeUrl = settings.GOOGLE['REVOKE_URL']

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getOauthLink(self):
        return (
            f"{self.loginUrl}?"
            f"client_id={self.clientId}&"
            f"redirect_uri={self.redirectUri}&"
            f"response_type=code&"
            f"scope=openid%20email%20profile&"
            f"access_type=offline&"
            f"prompt=consent"
        )
    def getAccessToken(self, code):
        accessTokenRequest = {
            'grant_type': 'authorization_code',
            'client_id': self.clientId,
            'redirect_uri': self.redirectUri,
            'code': code,
            'client_secret': self.clientSecret
        }

        response = requests.post(self.tokenRequestUri, data=accessTokenRequest)
        return response.json()

    def getUserInfo(self, accessToken):
        print("getUserInfo 진입")
        headers = {'Authorization': f'Bearer {accessToken}'}
        print(f" accessToken: {accessToken}")
        print(f" headers: {headers}")
        print(f" URL: {self.userInfoRequestUri}")
        response = requests.post(self.userInfoRequestUri, headers=headers)
        print(f"{response}")
        return response.json()

    def getWithdrawLink(self, accessToken):
        """
        구글 OAuth Revoke API 호출
        """
        print("getWithdrawLink() for withdraw - Google")

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = {
            "token": accessToken
        }

        response = requests.post(self.revokeUrl, params=payload, headers=headers)

        # 응답 확인
        if response.status_code == 200:
            return response.json()
        else:
            return response.text  # 에러 메시지 반환
