from django.db import models


# Create your models here.
class UserInfo(models.Model):
    userid = models.AutoField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    QQ = models.CharField(max_length=16)
    dreamCompany = models.CharField(max_length=32)
    language = models.CharField(max_length=16)
    registerTime = models.DateTimeField()
    delStatus = models.BooleanField(default=False)


class HomeworkInfo(models.Model):
    homeworkId = models.AutoField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=64)
    number = models.CharField(max_length=64)
    topicName = models.CharField(max_length=64)
    difficulty = models.CharField(max_length=16)
    times = models.IntegerField(default=1)
    comment = models.TextField(default="")
    recording = models.TextField()
    chineseIssue = models.TextField(default="")
    worldIssue = models.TextField(default="")
    delStatus = models.BooleanField(default=False)
