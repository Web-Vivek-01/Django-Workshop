from django.db import models
userTypeData = (
    ("Teacher","Teacher"),
    ("Student","Student")
)
userGender = (
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other")
)

class lmsUser(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,null=True,blank=True, choices=userGender)
    number = models.CharField(unique=True, max_length=10)
    userType = models.CharField(max_length=10,choices=userTypeData)

class courseUpload(models.Model):
    courseUploadId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=20)
    courseDescription = models.CharField(max_length=50)
    createdAt = models.DateField()
    coursePlaylist = models.IntegerField()
    courseDuration = models.CharField(max_length=10)
    userName = models.ForeignKey(lmsUser,on_delete=models.CASCADE)