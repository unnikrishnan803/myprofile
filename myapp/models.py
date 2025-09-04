from django.db import models

# Create your models here.

class Vlog(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    photo = models.ImageField(upload_to='vlog_photos/', blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    video = models.FileField(upload_to='project_videos/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key
