from django.db import models

class UserModel(models.Model):
    uno=models.IntegerField(primary_key=True)
    uname=models.CharField(max_length=30)
    contact=models.IntegerField()
    qualification=models.CharField(max_length=40)
    email=models.EmailField()
    proof=models.CharField(max_length=30)
class MedicienandDiseasesModel(models.Model):
    mdno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=30)
    medicines=models.CharField(max_length=30)


