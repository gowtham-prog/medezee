from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class gender(models.Model):
    Gender = models.CharField(max_length= 64)
    def __str__(self):
        return f"{self.Gender}"
class hospital(models.Model):
    Name = models.CharField(max_length= 100)
    Department= models.ManyToManyField('department', related_name= "h_speciality",blank= True)
    Doctor = models.ManyToManyField('doctor', related_name= "h_doctors",blank= True)
    Phone = models.CharField(max_length=12,null= False)
    place = models.ForeignKey('Location',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.Name}"


class department(models.Model):
    Name= models.CharField(max_length=64)
    Hospital = models.ManyToManyField(hospital,related_name= "dpt_hospitals",blank= True)
    Doctor = models.ForeignKey('doctor',on_delete= models.CASCADE,blank= True)

    def __str__(self):
        return f"{self.Name}"


class doctor(models.Model):
    Name = models.CharField(max_length=64)
    Department = models.ManyToManyField(department, related_name= "dr_speciality",blank= True)
    Hospital = models.ManyToManyField(hospital,related_name= "dr_hospitals",null=False,blank= True)
    Phone= models.CharField(max_length=12,null= False)
    
    def __str__(self):
        return f"{ self.Name}"

class Location(models.Model):
    Village = models.CharField(max_length =64)

class patient(models.Model):
    Name= models.CharField(max_length= 64)
    Age = models.IntegerField(null= False)
    Gender= models.ForeignKey(gender, on_delete= models.CASCADE,null= False,blank= True)
    Hospital = models.ForeignKey(hospital,on_delete= models.CASCADE,null= False,blank= True)
    Doctor = models.ForeignKey(doctor,on_delete= models.CASCADE,null= False,blank= True)
    Problem = models.CharField(max_length = 1000,null= False)
    Department = models.ForeignKey(department,on_delete= models.CASCADE,null= True,blank= True)
    Date = models.DateField()
    timestamp = models.TimeField()
    Active = models.BooleanField(default=True)
    Creator = models.ForeignKey(User,on_delete= models.CASCADE)
    def __str__(self):
        return f"{ self.Name}"
class test(models.Model):
    Patient = models.ForeignKey(patient,on_delete= models.CASCADE,blank= True)
    Test = models.CharField(max_length= 64)
    Name = models.CharField(max_length= 64)
    Date = models.DateField()
    Active = models.BooleanField(default=True)
    timestamp = models.TimeField()
    location = models.ForeignKey(Location,on_delete= models.CASCADE,blank= True)
    Creator = models.ForeignKey(User,on_delete= models.CASCADE)

class medicine(models.Model):
    Patient = models.ForeignKey(patient,on_delete= models.CASCADE,blank= True)
    medicine = models.CharField(max_length= 64)
    Name = models.CharField(max_length= 64)
    Delivery = models.CharField(max_length=64)
    location = models.ForeignKey(Location,on_delete= models.CASCADE,blank= True)
    Date = models.DateField()
    Active = models.BooleanField(default=True)
    Creator = models.ForeignKey(User,on_delete= models.CASCADE)
