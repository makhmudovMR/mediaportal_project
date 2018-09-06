from django.views.generic.list import MultipleObjectMixin
from .models import Category, Article

'''
Класс примеси моделей
'''


class CategoryAndArticlesListMixin(MultipleObjectMixin):

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['categories'] = Category.objects.all()
        context['tabs_articles'] = Article.objects.all()
        return context