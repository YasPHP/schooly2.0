from django.db import models

class Schedule(models.Model):
    activity_name = models.CharField(max_length=200)
    activity_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.activity_name
