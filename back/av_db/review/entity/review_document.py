from django.db import models

from review.entity.review import Review


class ReviewDocument(models.Model):
    id = models.AutoField(primary_key=True)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, db_column='review_id')

    class Meta:
        db_table = 'review_document'
        app_label = 'review'