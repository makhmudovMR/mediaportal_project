from django.db import models
from django.urls import reverse


def generate_filename(instance, filename):
	filename = instance.slug + '.jpg'
	return f'{instance}/{filename}'


class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField()

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
	dislake = models.PositiveIntegerField(default=0)

	objects = models.Manager()

	def __str__(self):
		return str(self.title)


'''class MyArticles(Article):

	class Meta:
		proxy = True'''

