from django.db import models

# Create your models here.
class Stock(models.Model):
	ticker = models.CharField(max_length=10,primary_key=True)

	def __str__(self):
		return self.ticker

		