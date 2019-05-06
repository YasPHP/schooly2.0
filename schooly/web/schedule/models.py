from django.db import models
from django.utils import timezone

class Schedule(models.Model)
    activity_title = models.Charfield(max_Length=200)
    activity_content = models.TextField()
    activity_date = models.DateTimeField("Date of Activity", default=datetime.now)

    def schedule_status(Self):
        "Returns the flashcard's completion status."
        import datetime
        if self.activity