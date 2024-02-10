from django.db import models
class student(models.Model):
  name = models.CharField(max_length=255)
  Age = models.IntegerField()
  Department = models.CharField(max_length=255)
  img=models.ImageField(upload_to="student/img")

  def __str__(self):
    return self.name
# Create your models here.
