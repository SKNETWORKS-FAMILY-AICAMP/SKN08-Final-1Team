import uuid

from django.db import transaction
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK


from account.service.account_service_impl import AccountServiceImpl
from account_profile.service.account_profile_service_impl import AccountProfileServiceImpl
from naver_oauth.serializer.naver_oauth_access_token_serializer import NaverOauthAccessTokenSerializer
from naver_oauth.service.naver_oauth_service_impl import NaverOauthServiceImpl
from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


class NaverOauthController(viewsets.ViewSet):
    naverOauthService = NaverOauthServiceImpl.getInstance()
    redisCacheService = RedisCacheServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    accountProfileService = AccountProfileServiceImpl.getInstance()

    def requestNaverOauthLink(self, request):
        url = self.naverOauthService.requestNaverOauthLink()

        return JsonResponse({"url": url}, status=status.HTTP_200_OK)

    def requestAccessToken(self, request):
        print("진입")
        try:
            print(f"{request.data}")
            code = request.data['code']['code']
            state = request.data['code']['state']
        except KeyError as e:
            print(f"KeyError: {e}")
            return Response({"error": f"Missing key: {str(e)}"}, status=400)
        print(f"값은:{code}")
        print(f"두번째: {state}")
        serializer = NaverOauthAccessTokenSerializer(data={'code': code, 'state': state})
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']
        state = serializer.validated_data['state']
        print(f"code: {code}, state: {state}")

        try:
            tokenResponse = self.naverOauthService.requestNaverAccessToken(code, state)
            print("완료")
            accessToken = tokenResponse['access_token']
            print(f"accessToken: {accessToken}")

            with transaction.atomic():
                userInfo = self.naverOauthService.requestUserInfo(accessToken)
                print(f"{userInfo}")
                response_data = userInfo.get('response',{})
                user_id = response_data.get('id', '')  # 사용자 ID
                nickname = response_data.get('nickname', '')  # 닉네임
                email = response_data.get('email', '')  # 이메일
                gender = {"M": "male", "F": "female"}.get(response_data.get('gender', ''), '')  # 성별
                age_range = response_data.get('age', '')  # 연령대
                birthyear = response_data.get('birthyear', '')  # 출생연도
                loginType = 'NAVER'
                # 정보 출력 (디버깅용)
                print(f"user_id: {user_id}, email: {email}, nickname: {nickname}")
                print(f"gender: {gender}, age_range: {age_range}, birthyear: {birthyear}")

                # 이메일 중복 확인
                account = self.accountService.checkEmailDuplication(email)
                print(f"account: {account}")

                if account is None:
                    account = self.accountService.createAccount(email, loginType)
                    print(f"accountProfile: {account}")
                    accountProfile = self.accountProfileService.createAccountProfile(
                        account.getId(), nickname, gender, birthyear, age_range
                    )

                    print(f"accountProfile: {accountProfile}")

                userToken = self.__createUserTokenWithAccessToken(account, accessToken)
                print(f"userToken: {userToken}")

            return JsonResponse({'userToken': userToken})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


    def requestUserToken(self, request):
        #global accountProfile
        global account
        access_token = request.data.get('access_token')  # 클라이언트에서 받은 access_token
        user_id = request.data.get('user_id')# 클라이언트에서 받은 id
        email = request.data.get('email')  # 클라이언트에서 받은 email
        nickname = request.data.get('nickname')  # 클라이언트에서 받은 nickname
        gender = request.data.get('gender', '')  # 클라이언트에서 받은 성별
        age_range = request.data.get('age_range', '')  # 클라이언트에서 받은 연령대
        birthyear = request.data.get('birthyear', '')  # 클라이언트에서 받은 출생연도
        loginType = 'NAVER'
        print(f"{request.data}")

        if not access_token:
            return JsonResponse({'error': 'Access token is required'}, status=400)

        if not user_id or not email or not nickname :
            return JsonResponse({'error': 'All user information (ID, email, nickname, gender, age_range, birthyear) is required'}, status=400)

        try:
            # 이메일을 기반으로 계정을 찾거나 새로 생성합니다.
            print('acquire data!')
            account = self.accountService.checkEmailDuplication(email)
            print(f'account: {account}')

            if account is None:
                print("There are no account!")
                account = self.accountService.createAccount(email, loginType)
                accountProfile = self.accountProfileService.createAccountProfile(
                    account.getId(), nickname, gender, birthyear, age_range
                )

            print("ready to create userToken")
            # 사용자 토큰 생성 및 Redis에 저장
            userToken = self.__createUserTokenWithAccessToken(account, access_token)

            return JsonResponse({'userToken': userToken})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def __createUserTokenWithAccessToken(self, account, accessToken):
        try:
            userToken = str(uuid.uuid4())
            self.redisCacheService.storeKeyValue(account.getId(), accessToken)
            self.redisCacheService.storeKeyValue(userToken, account.getId())

            if not account or not account.getId():
                raise ValueError("Invalid account ID")

            return userToken

        except Exception as e:
            print('Redis에 토큰 저장 중 에러:', e)
            raise RuntimeError('Redis에 토큰 저장 중 에러')


    # def dropRedisTokenForLogout(self, request):
    #     try:
    #         userToken = request.data.get('userToken')
    #         isSuccess = self.redisService.deleteKey(userToken)
    #
    #         return Response({'isSuccess': isSuccess}, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         print('레디스 토큰 해제 중 에러 발생:', e)
    #         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
