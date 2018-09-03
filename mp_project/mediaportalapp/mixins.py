from django.views.generic.list import MultipleObjectMixin
from .models import Category

'''
Класс примеси моделей
'''


class CategoryListMixin(MultipleObjectMixin):

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['categories'] = Category.objects.all()
        return context