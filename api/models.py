from django.db import models
from django.utils import timezone
# Create your models here.


class Profile(models.Model):
	idno = models.IntegerField(primary_key=True,blank=False)
	name=models.CharField(max_length=200,default="RandomUser")
	email=models.CharField(max_length=200,default="RandomUser@gmail.com")
	image = models.ImageField(upload_to='profile_pics',blank=True)
	password=models.CharField(max_length=200,default="newuser")


class Tag(models.Model):
	to = models.IntegerField()
	fromm = models.IntegerField()
	vote_from = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	tagcontent = models.CharField(max_length=200)


class Scrib(models.Model):
	to = models.IntegerField()
	scrib_from = models.IntegerField()
	date_posted = models.DateTimeField(default=timezone.now)
	scribcontent = models.TextField()




class Ques(models.Model):
	to = models.IntegerField()
	vote_from = models.TextField()
	quescontent = models.TextField()






