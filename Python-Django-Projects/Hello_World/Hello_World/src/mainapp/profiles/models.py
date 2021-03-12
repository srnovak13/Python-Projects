from django.db import models

NAME_PREFIX = {
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Miss', 'Miss'),
    ('Dr', 'Dr'),
}


# Create your models here.
class UserProfile(models.Model):
    name_preface = models.CharField(max_length=30, default="", null=False, choices=NAME_PREFIX)
    first_name = models.CharField(max_length=30, default="", null=False)
    last_name = models.CharField(max_length=50, default="", null=False)
    email = models.CharField(max_length=60, null=False)
    username = models.CharField(max_length=60, default="", null=False)

    objects = models.Manager()

    def __str__(self):
        return self.username

