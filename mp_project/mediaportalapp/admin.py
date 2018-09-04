from django.contrib import admin
from .models import Category, Article, Comments



class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments)