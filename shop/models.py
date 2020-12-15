from django.db import models
from datetime import date
# Create your models here.
class Product(models.Model):
    product_id= models.AutoField
    product_name=models.CharField(max_length=20,default="")
    category= models.CharField(max_length =20,default="")
    subcategory=models.CharField(max_length=50,default="")
    price= models.IntegerField(default=0)
    desc= models.CharField(max_length=300,default="")
    pub_date= models.DateField(default=date.today)
    image= models.ImageField(upload_to="shop/image",default="")    
    
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=40, default="")
    email= models.CharField(max_length=40,default="")
    desc= models.CharField(max_length=300 ,default="")
    def __str__(self):
         return self.name
class Order(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount= models.IntegerField( max_length=100, default=0)
    name= models.CharField(max_length=30)
    email= models.CharField(max_length=100)
    address= models.CharField(max_length=111)
    city=models.CharField(max_length=120)
    state= models.CharField(max_length=30)
    phone=models.CharField(max_length=243, default="")
    zip_code= models.CharField(max_length=1333, default="")
    def __str__(self):
        return self.name
    def getid(self):
        return self.order_id
    
class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."