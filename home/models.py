from django.db import models

# Create your models here.

class Register(models.Model):
  name = models.CharField(max_length=30)
  phone = models.CharField(max_length=20)
  email = models.EmailField()
  group = models.CharField(max_length=20)
  college = models.CharField(max_length=30)

  def __str__(self):
      # return "" + +self.name + " " + self.phone + " " + str(self.email) + " "+ self.group + " " + self.college 
      return f"Name={self.name},   phone={self.phone},   Email={self.email},   Group={self.group},   College={self.college}"


