from django.db import models

# Create your models here.
class CrudModel(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=13,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    hobiy=models.CharField(max_length=100,null=True,blank=True)
    body=models.TextField(null=True,blank=True)
    img=models.ImageField(upload_to='img',null=True,blank=True)
    def __str__(self) -> str:
        return self.first_name
