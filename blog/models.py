from django.db import models
from django.core.urlresolvers import reverse
import datetime

class Lyrics(models.Model):
	title = models.CharField(max_length=150, blank=False)
	date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to="uploads/", help_text="100 X 100 images")

	def admin_image(self):
		return '<img src="%s" height="100" width="100"/>' %self.image.url
	admin_image.allow_tags = True
	admin_image.short_description = "Image"


	def __unicode__(self):
		return self.title


	class Meta:
		verbose_name_plural = 'Lyrics'
		
	

class Poems(models.Model):
	title = models.CharField(max_length=100, blank=False)
	date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to="uploads/", help_text="100 X 100 images")

	def admin_image(self):
		return '<img src="%s" height="100" width="100"/>'%self.image.url
	admin_image.allow_tags = True
	admin_image.short_description = "Image"

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Poems'

	

class ShortStory(models.Model):
	title = models.CharField(max_length=100, blank=False)
	date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to="uploads/", help_text="100 X 100 images")

	def admin_image(self):
		return '<img src="%s" height="100" width="100"/>'%self.image.url
		admin_image.allow_tags = True
		admin_image.short_description = "Image"

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Short Stories'


class Blog(models.Model):
	title = models.CharField(max_length=100, blank=False)
	date = models.DateTimeField()
	content = models.TextField()

	def __unicode__(self):
		return self.title






