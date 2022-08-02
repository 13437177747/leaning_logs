import imp
from django.contrib import admin

from learning_logs.models import Topic

# Register your models here.
from .models import Topic,Entry

admin.site.register(Topic)
admin.site.register(Entry)