from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from product.models import Product

# usermanager for the custom user model
class Usermanager(BaseUserManager):
	def create_user(self, first_name, last_name, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
            first_name= first_name,
            last_name= last_name,
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, first_name, last_name, email, username, password):
		user = self.create_user(
            first_name= first_name,
            last_name= last_name,
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

# user model to store user's data
class User(AbstractBaseUser):
    first_name              = models.CharField(max_length=50)
    last_name               = models.CharField(max_length=50)
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username 				= models.CharField(max_length=30, unique=True)
    wishlist_items          = models.ManyToManyField(Product, blank=True, related_name="wishlist_items")
    cart_items              = models.ManyToManyField(Product, blank=True, related_name="cart_items")
    ordered_items           = models.ManyToManyField(Product, blank=True, related_name="ordered_items")
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'  # sign in through email address
    REQUIRED_FIELDS = ['first_name', 'last_name','username']
    
    objects = Usermanager() # manager to be used to handle the model

    #Returns the query into the model 
    
    def __str__(self):
        return self.email
        
    # For checking permissions. Admin have all the permissons.
    
    def has_perm(self, perm, obj=None): 
        return self.is_admin

	# Does the user have permission to view this app? Yes.
    def has_module_perms(self, app_label):
        return True
