from django.contrib import admin

# Register your models here.

from .models import PostAd, ExtentionUser

admin.site.register(ExtentionUser)
admin.site.register(PostAd)
