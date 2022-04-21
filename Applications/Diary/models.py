from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Diary(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField(blank = True, null = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return (self.name)    

class Chapter(models.Model):
    diary = models.ForeignKey(Diary, on_delete = models.CASCADE)
    name = models.CharField(max_length = 250)
    summary = models.CharField(max_length = 500, blank = True, null = True)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return (self.name)    

    
