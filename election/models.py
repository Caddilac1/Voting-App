from django.db import models

class voters(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Other_Name = models.CharField(max_length=100, blank=True, null=True)
    Form = models.IntegerField()
    Index_Number = models.CharField(max_length=20, unique=True, primary_key=True)
    Token = models.CharField(max_length=8, unique=True,null=True)
    is_token_used = models.BooleanField(default=False)

    

    class Meta:
        db_table = 'voters'

    






class candidates(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Other_Name = models.CharField(max_length=100,null=True, blank=True)
    Votes = models.IntegerField(default=0)

    class Meta:
        db_table = 'candidates'


    
     

     