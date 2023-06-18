from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Item(models.Model):
	# relations FK are many to many. category is the Category for an item. And all items under a Category can be accessed.
	#Similarly, created_by a User and all items created_by one user can be accessed.
	category = models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	price = models.FloatField()
	image = models.ImageField(upload_to='item_img', blank=True, null=True)
	is_sold = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, related_name = 'items', on_delete=models.CASCADE)

	def __str__(self):
		return self.name


