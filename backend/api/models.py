from django.db import models
from django.contrib.auth.models import User

class Position(models.Model):
    CompanyName = models.CharField(max_length=50)
    PosName = models.CharField(max_length=50)
    City = models.CharField(max_length=50)

    def __str__(self):
        return self.PosName

class Apply(models.Model):
    User_Name = models.ForeignKey(User,on_delete=models.CASCADE)
    Pos_Name = models.ForeignKey(Position,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.User_Name} - {self.Pos_Name.PosName}"