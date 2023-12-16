from django.db import models
#https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title