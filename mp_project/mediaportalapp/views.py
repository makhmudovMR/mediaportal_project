from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, Category


class ArticleListView(ListView):

	model = Article
	template_name = 'mediaportalapp/index.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['articles'] = self.model.objects.all()
		return context



class CategoryListView(ListView):

	model = Category
	template_name = 'mediaportalapp/index.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['categories'] = self.model.objects.all()
		return context


class CategoryDetailView(DetailView):
	model = Category
	template_name = 'mediaportalapp/category_detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		# context['categories'] = self.models.objects.all()
		# context['category'] = self.get_object()
		return context
