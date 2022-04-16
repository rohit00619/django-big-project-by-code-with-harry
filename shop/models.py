from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category =models.CharField(max_length=50, default="")
    subcategory =models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='Shop/images',default="")


    def __str__(self):
        return self.product_name

class Stores(models.Model):
    store_id = models.AutoField
    store_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50,default='')
    country = models.CharField(max_length=50, default='')
    contactnumber = models.IntegerField(default=0000000000)
    image = models.ImageField(upload_to='Shop/images', default="")

    def __str__(self):
        return self.store_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=70, default="")
    phone= models.IntegerField(default=0000000000)
    desc = models.CharField(max_length=1000,default='No Desc')

    def __str__(self):
        return self.name


class Signup(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=15)
    username=models.CharField(max_length=50)
    userpassword=models.CharField(max_length=50)

    def __str__(self):
        return self.name





class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000, default='')
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip_code=models.CharField(max_length=15)
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.items_json[0:100]



class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default='')
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:15] + "..."
