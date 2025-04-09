from template.request_generator.base_request import BaseRequest
from user_defined_protocol.protocl import UserDefinedProtocolNumber


class MakingReportRequest(BaseRequest):

    def __init__(self, **kwargs):
        self.__protocolNumber = UserDefinedProtocolNumber.REPORT_MAKING.value

    # 사용자 정의 프로토콜 => 사용자가 임의로 번호를 임의로 지정하여 프로토콜을 사용합니다.
    def getProtocolNumber(self):
        return self.__protocolNumber

    def toDictionary(self):
        return {
            "protocolNumber": self.__protocolNumber
        }

    def __str__(self):
        return f"MakingReportRequest(protocolNumber={self.__protocolNumber}"