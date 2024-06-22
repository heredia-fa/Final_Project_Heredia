from django.contrib import admin
from  landing_news.models import *


class NewsAdmin(admin.ModelAdmin):
  list_display = ['title', 'date', "original_date"]




# Register your models here.
admin.site.register(News ,NewsAdmin)