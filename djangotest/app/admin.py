from django.contrib import admin
from .models import News, Category, Feedback, Profile

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Feedback)

# Register your models here.
