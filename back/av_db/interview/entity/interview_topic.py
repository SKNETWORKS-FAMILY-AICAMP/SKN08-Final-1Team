from django.db import models


class InterviewTopic(models.TextChoices):
    BACKEND = "Backend", "백엔드"
    FRONTEND = "Frontend", "프론트엔드"
    EMBEDDED = "Embedded", "임베디드"
    AI = "AI", "인공지능"
    DEVOPS = "DevOps", "데브옵스"
    WEBAPP = "AppWeb", "앱웹"
