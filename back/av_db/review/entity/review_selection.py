from django.db import models

from review.entity.review_question import ReviewQuestion


class ReviewSelection(models.Model):
    id = models.AutoField(primary_key=True)
    selection = models.CharField(max_length=50, unique=False)
    review_question_id = models.ForeignKey(ReviewQuestion, on_delete=models.CASCADE, db_column='review_question_id')

    class Meta:
        db_table = 'review_selection'
        app_label = 'review'