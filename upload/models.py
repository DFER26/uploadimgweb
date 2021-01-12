from django.db import models
# models.py
class images(models.Model):
	name = models.CharField(max_length=50)
	Main_Img = models.ImageField(upload_to='images/')
	Snd_Img = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name

# Create your models here.
