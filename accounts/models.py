from django.db import models
class user_info(models.Model):
    address=models.CharField(max_length=200,blank=True,null=True)
    phone_number=models.CharField(max_length=20,blank=True, null=True)
class profile(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=51, blank=True, null=True)
    waiting_time=models.DecimalField( max_digits=5, decimal_places=2)
    subtitle=models.TextField(max_length=500,blank=True,null=True)
    doctor_specialist=''
    photos=models.ImageField(upload_to='doc_photo/')
    clinics_photo=models.ImageField(upload_to='photo/')
    date_of_creating_profile=models.DateField()
    price=models.IntegerField()
    working_hours=models.DecimalField( max_digits=5, decimal_places=2)