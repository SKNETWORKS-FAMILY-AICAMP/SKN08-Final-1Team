from user_defined_protocol.protocol import UserDefinedProtoclNumber


class MakingReportResponse:

    def __init__(self, responseData):
        self.protoclNumber = UserDefinedProtoclNumber.REPORT_MAKING.value

        for key, value in responseData.items():
            setattr(self, key, value)

    @classmethod
    def fromResponse(cls, responseData):
        return cls(responseData)

    def toDictionary(self):
        return self.__dict__

    def __str__(self):
        return f"MakingReportResponse({self.__dict__})"