from django.db import models

class Filing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    filing_date = models.DateField()

    def __str__(self):
        return self.title
