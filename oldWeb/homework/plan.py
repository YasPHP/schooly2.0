from django.db import models

class Homework(models.Model):
    homework_title = models.CharField(max_length=200)

class Work(models.Model):
    """
    A Work object that holds the information and characteristics of a student's homework.

    Presents attributes of work object based on options which the user fills in via a from.
    The attribute is a added to a form that acts as an indicator of work type to the user.

    Attributes
    ----------
     course: str
           The course name of the student's work
     title: str
          The title of the student's work 
    body: str
        The body description of the student's work 
    """
    course = models.ForeignKey(note_title)
    title = models.CharField(max_length=200)
    body = models.TextField()
    due_date = models.DateTimeField()
    completion_status = Boolean()

    #query it like django
    Entry.filter(note_name= input)

    def __str__(self):
        return self.Work
        """
        Returns
        -------
        None
        """

