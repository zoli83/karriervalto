from django.db import models

#Létrehozott táblák
#	Munkáltató => Company
#   Munkavállaló => RegisteredUser
#	Meghirdetett állások => Position
#	Jelentkezés => Apply


class RegisteredUser(models.Model):
    Name = models.CharField(max_length=255)
    City = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Company(models.Model):
    CompanyName = models.CharField(max_length=50)
    CompanyEmail = models.CharField(max_length=50)
    CompanyMobile = models.CharField(max_length=50)

    def __str__(self):
        return self.CompanyName

class Position(models.Model):
    CompanyName = models.ForeignKey(Company,on_delete=models.CASCADE)
    PosName = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    City = models.CharField(max_length=50)

    def __str__(self):
        return self.PosName

class Apply(models.Model):
    User_Name = models.ForeignKey(RegisteredUser,on_delete=models.CASCADE)
    Pos_Name = models.ForeignKey(Position,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.User_Name.Name + " - "+ self.Pos_Name.PosName