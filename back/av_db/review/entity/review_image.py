from django.db import models

from review.entity.review_question import ReviewQuestion

class ReviewImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.TextField(null=True)
    question_id = models.ForeignKey(ReviewQuestion, on_delete=models.CASCADE, db_column='question_id', unique=False)

    class Meta:
        db_table = 'review_image'
        app_label = 'review'