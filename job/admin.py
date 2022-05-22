from django.contrib import admin


# Register your models here.

from .models import Job, Category, Candidate

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Candidate)
