from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.course_id} : {self.course_name}'