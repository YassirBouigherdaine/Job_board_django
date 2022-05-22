from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
from operator import mod
from pickle import TRUE
from django.db import models

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

# Create your models here.

class Job(models.Model):
    user = models.ForeignKey(User, related_name='job_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    Job_Type = models.CharField(max_length=20, choices=JOB_TYPE)
    published_at = models.DateField(auto_now=TRUE)
    description = models.TextField(max_length=1000)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to='job/')
    location = models.CharField(max_length=60)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
       return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Job, self).save(*args, **kwargs)



class Category(models.Model):
    name = models.CharField(max_length=20)    

    def __str__(self):
        return self.name   


class Candidate(models.Model):

    job = models.ForeignKey(Job, related_name='candidate', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    apply_at = models.DateField(auto_now=TRUE)
    website = models.URLField()
    cv = models.FileField(upload_to='candidate/')
    coverLetter = models.FileField(upload_to='candidate/')
    
    def __str__(self):
        return self.name 