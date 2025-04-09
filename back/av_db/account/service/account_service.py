from abc import ABC, abstractmethod


class AccountService(ABC):

    # DB 생성
    @abstractmethod
    def createAccount(self, email, loginType):
        pass
    @abstractmethod
    def createAdminAccount(self, email, loginType):
        pass
    @abstractmethod
    def createWithdrawalAccount(self, accountId):
        pass


    # 이메일 중복확인
    @abstractmethod
    def checkEmailDuplication(self, email):
        pass


    # MyPage 수정칸
    @abstractmethod
    def findEmail(self, accountId):
        pass

    @abstractmethod
    def createWithdrawAt(self, time):
        pass

    @abstractmethod
    def createWithdrawEnd(self, time):
        pass


    # 회원탈퇴
    @abstractmethod
    def withdraw(self, accountId: int) -> bool:
        pass
