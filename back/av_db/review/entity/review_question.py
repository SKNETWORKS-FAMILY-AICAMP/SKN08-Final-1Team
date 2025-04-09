from django.db import models

from review.entity.review import Review


class ReviewQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=128, unique=False)
    question_type = models.CharField(max_length=10)
    essential = models.BooleanField()
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, db_column='review_id')

    class Meta:
        db_table = 'review_question'
        app_label = 'review'