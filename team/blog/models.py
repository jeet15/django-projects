from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length = 140)
	description = models.CharField(max_length=140)
	content = models.TextField()
	slug  = models.BooleanField(default=True)
	published = models.DateTimeField(auto_now_add = True)
	created = models.ForeignKey(User, null=True)
	author = models.URLField(blank = True)
	link = models.URLField(blank=True)
	link_description = models.CharField(max_length = 140 , blank = True)


	class Meta:
		ordering = ['-created']

	def __str__(self)	:
		return self.title

	def get_absolute_url(self):
		return reverse('get-blog', kwargs={'slug': self.slug })

class Comment(models.Model):
	post = models.ForeignKey(Post)
	name = models.CharField(max_length=20)
	text = models.CharField(max_length = 200)
	timestamp = models.DateTimeField(auto_now_add = True)




# Create your models here.
