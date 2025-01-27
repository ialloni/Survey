from django.contrib import admin
from .models import Survey, PostQuestion, PostAnswer
# Register your models here.

@admin.register(Survey)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    search_fields = ('title', 'slug', 'publish')
    list_filter = ('title', 'slug', 'publish')


@admin.register(PostQuestion)
class PostQuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(PostAnswer)
class PostAnswerAdmin(admin.ModelAdmin):
    pass