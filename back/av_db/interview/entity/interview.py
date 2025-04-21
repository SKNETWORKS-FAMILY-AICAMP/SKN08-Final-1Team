from django.db import models
from account.entity.account import Account
from interview.entity.experience_level import ExperienceLevel
from interview.entity.interview_status import InterviewStatus
from interview.entity.interview_topic import InterviewTopic


class Interview(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="interviews")
    topic = models.CharField(
        max_length=50,
        choices=InterviewTopic.choices
    )
    experience_level = models.IntegerField(
        choices=ExperienceLevel.choices,
    )
    status = models.CharField(
        max_length=20,
        choices=InterviewStatus.choices,
        default=InterviewStatus.IN_PROGRESS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'interview'
        app_label = 'interview'

    def __str__(self):
        return f"Interview(id={self.id}, account={self.account}, topic={self.topic}, experience_level={self.experience_level}, status={self.status})"

    def getId(self):
        return self.id

    def getAccount(self):
        return self.account

    def getTopic(self):
        return self.topic

    def getExperienceLevel(self):
        return ExperienceLevel(self.experience_level)

    def getStatus(self):
        return self.status

    def getCreatedAt(self):
        return self.created_at