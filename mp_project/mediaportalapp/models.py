from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.conf import settings

def generate_filename(instance, filename):
	filename = instance.slug + '.jpg'
	return u'{0}/{1}'.format(instance.slug, filename)


class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField()

	# получаем ссылку на категории
	def get_absolute_url(self):
		return reverse('category_detail_mediaportalapp', kwargs={'slug': self.slug})

	def __str__(self):
		return str(self.name)



class Article(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=150)
	slug = models.SlugField()
	image = models.ImageField(upload_to=generate_filename)
	content = models.TextField()
	likes = models.PositiveIntegerField(default=0)
	dislikes = models.PositiveIntegerField(default=0)
	comments = GenericRelation('comments')
	user_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

	objects = models.Manager()

	def get_absolute_url(self):
		return reverse('article_detail_mediaportalapp', kwargs={'slug': self.slug})

	def __str__(self):
		return str(self.title)



class Comments(models.Model):

	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	comment = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey()

