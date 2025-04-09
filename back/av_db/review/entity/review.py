from django.db import models

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    review = models.CharField(max_length=128)

    def __str__(self):
        return f"Review -> id: {self.id}"


    class Meta:
        db_table = 'review'
        app_label = 'review'