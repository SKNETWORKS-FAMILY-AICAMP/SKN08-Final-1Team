from pydantic import BaseModel


class QuestionGenerationRequest(BaseModel):
    interviewId: int
    topic: str  # JobCategory에서 변환된 값
    experienceLevel: str  # ExperienceLevel에서 변환된 값
    userToken: str