from django.db import models

# Create your models here.

class UserInfo(models.Model):
	username = models.CharField(max_length=200)
	country = models.CharField(max_length=200,blank=True)
	mozillian_date = models.DateTimeField(blank=True,null=True)
	url = models.URLField(blank=True)

class Skill(models.Model):
	skill_id = models.IntegerField(default=0)
	username = models.CharField(max_length=200, blank=True)
	skill_name = models.CharField(max_length=200)
	member_count = models.IntegerField(blank=True)

class UserSkill(models.Model):
	username = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	skill = models.CharField(max_length=200)