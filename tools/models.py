from django.db import models

class PersponalityDetails(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	date = models.DateField()
	picture = models.ImageField(upload_to='media')
	software = models.TextField(blank=False)
	hardware = models.TextField(blank=False)
	dream_setup = models.TextField(blank=False)


	
	def __unicode__(self):
		return self.name