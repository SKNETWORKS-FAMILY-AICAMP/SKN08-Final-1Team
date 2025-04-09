from django.db import models
from review.entity.review import Review


class ReviewDescription(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, unique=False)
    review_id = models.OneToOneField(Review, on_delete=models.CASCADE, db_column='review_id')

    class Meta:
        db_table = 'review_description'
        app_label = 'review'