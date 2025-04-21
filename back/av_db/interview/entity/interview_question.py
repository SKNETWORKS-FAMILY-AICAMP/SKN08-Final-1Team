from django.db import models

class InterviewQuestion(models.Model):
    interview = models.ForeignKey("Interview", on_delete=models.CASCADE, related_name="questions")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'interview_question_data'
        app_label = 'interview'