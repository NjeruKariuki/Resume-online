from email.mime import image
from django.db import models


#technologies
class Technology(models.Model):
    name = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return self.name + ' created'

class Project(models.Model):
    name = models.CharField(max_length=50)
    technologies = models.ManyToManyField(Technology, blank=True)
    description = models.TextField(max_length=500, blank=True)
    git_link = models.CharField(max_length=200, blank=True)
    images = models.ManyToManyField(ProjectImage, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return self.name

