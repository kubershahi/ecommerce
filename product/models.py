from django.db import models

# Create your models here.

# class Category(models.Model):
# 	categor_type = models.CharField(max_length=30)

class Product(models.Model):
	product_id	= models.AutoField
	image 		= models.ImageField(upload_to ="product/images", null=True)
	title 		= models.CharField(max_length=120)
	summary		= models.TextField(blank=True, null=False)
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(decimal_places=2, max_digits=1000)
	category	= models.CharField(max_length=120,null=True)
	sub_category = models.CharField(max_length=120,null=True)
	age			= models.CharField(max_length=120,null=True)
	date_modified = models.DateTimeField(auto_now=True)
	

	def __str__ (self):
		return self.title