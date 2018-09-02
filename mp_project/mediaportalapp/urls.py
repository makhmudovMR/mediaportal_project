from django.conf.urls import url
from .views import ArticleListView, CategoryDetailView, CategoryListView



urlpatterns = [
	url(r'^$', CategoryListView.as_view(), name='index_mediaportalapp'),
	url(r'category/(?P<slug>[-\w]+)/', CategoryDetailView.as_view(), name='category_detail_mediaportalapp'),
]