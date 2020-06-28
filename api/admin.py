from django.contrib import admin

# Register your models here.

from .models import Profile,Ques,Scrib,Tag

admin.site.register(Profile)
admin.site.register(Ques)
admin.site.register(Scrib)
admin.site.register(Tag)