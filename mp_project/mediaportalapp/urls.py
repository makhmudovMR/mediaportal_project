from django.conf.urls import url
from .views import *



urlpatterns = [
	url(r'^$', CategoryListView.as_view(), name='index_mediaportalapp'),
	url(r'category/(?P<slug>[-\w]+)/', CategoryDetailView.as_view(), name='category_detail_mediaportalapp'),
	url(r'articles/(?P<category>[-\w]+)/(?P<slug>[-\w]+)', ArticleDetailView.as_view(), name='article_detail_mediaportalapp'),
	url(r'show_article_image/', DynamicArticleImageView.as_view(), name='show_article_image'),
	url(r'add_comment/', CreateCommentView.as_view(), name='add_comment'),
	url(r'get_articles_for_tabs_on_index_pages', DisplayArticleByCategoryView.as_view(), name='index_articles_mediaportalapp'),
	url(r'user_reaction/', UserReactionView.as_view(), name='user_reaction')
]