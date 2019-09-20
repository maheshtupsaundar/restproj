from django.db import models

class Product(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=30)
    pcost=models.DecimalField(max_digits=10,decimal_places=2)
    pmfdt=models.DateField()
    pexpdt=models.DateField()

