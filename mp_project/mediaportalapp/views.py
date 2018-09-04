from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.views import View
from .models import Article, Category
from .mixins import CategoryListMixin
from .forms import CommentForm

'''Это классы отвечающие за вывод информации на дисплей'''
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
		context['articles'] = Article.objects.all()[:4]
		return context


class CategoryDetailView(DetailView, CategoryListMixin):
	model = Category
	template_name = 'mediaportalapp/category_detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['category'] = self.get_object()
		context['articles_from_category'] = self.get_object().article_set.all()
		return context


class ArticleDetailView(DetailView, CategoryListMixin):
	model = Article
	template_name = 'mediaportalapp/article_detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['article'] = self.get_object()
		context['article_comments'] = self.get_object().comments.all()
		context['comment_form'] = CommentForm()
		return context


class DynamicArticleImageView(View):

	def get(self, *args, **kwargs):
		article_id = self.request.GET.get('article_id')
		article = Article.objects.get(id=article_id)
		data = {
			'article_img': article.image.url
		}
		return JsonResponse(data)


class CreateCommentView(View):
	template_name = 'article_detail.html'

	def post(self, request, *args, **kwargs):
		article_id = self.request.POST.get('article_id')
		comment = self.request.POST.get('comment')
		article = Article.objects.get(id=article_id)
		new_comment = article.comments.create(author=request.user, comment=comment)
		comment = [{
			"author": new_comment.author.username,
			"comment": new_comment.comment,
			"timestamp": new_comment.timestamp.strftime('%Y-%m-%d')
		}]
		return JsonResponse(comment, safe=False)

