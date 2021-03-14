from django.db import models

# Create your models here.


# This class sets up the objects that are mapped to the database. You have to make migrations when you edit this
class DjangoClasses(models.Model):
    title = models.CharField(max_length=50)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=50)
    duration = models.FloatField(max_length=4)

    objects = models.Manager()

# This determines what to show you when you call the object
    def __str__(self):
        return "{}".format(self.title)

