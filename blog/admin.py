from django.contrib import admin
from .models import  Article ,Comment ,Category ,Tag ,Like,Article_tag
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Article_tag)
