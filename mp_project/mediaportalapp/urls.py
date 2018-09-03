from django.conf.urls import url
from .views import ArticleListView, CategoryDetailView, CategoryListView, ArticleDetailView, dynamic_article_image



urlpatterns = [
	url(r'^$', CategoryListView.as_view(), name='index_mediaportalapp'),
	url(r'category/(?P<slug>[-\w]+)/', CategoryDetailView.as_view(), name='category_detail_mediaportalapp'),
	url(r'(?P<category>[-\w]+)/(?P<slug>[-\w]+)', ArticleDetailView.as_view(), name='article_detail_mediaportalapp'),
	url(r'show_article_image/', dynamic_article_image, name='show_article_image')
]