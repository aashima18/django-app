from django.db import models

# Create your models here.

class Organisation(models.Model):
  objects = models.Manager()
  name = models.CharField(max_length=60)

  def __str__(self):
        return self.name


class Courses(models.Model):
    objects = models.Manager()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

   





class Student(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True)
    courses = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name  