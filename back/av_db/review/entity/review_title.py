from django.db import models

from review.entity.review import Review


class ReviewTitle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, unique=False)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, db_column='review_id')

    class Meta:
        db_table = 'review_title'
        app_label = 'review'