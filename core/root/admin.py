from django.contrib import admin
from .models import Blog, News
from django.utils.html import format_html


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'is_published', 'photo_tag']
    list_editable = ['is_published']
    list_display_links = ['id', 'title']

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width=80 height=auto>')
        else:
            return format_html('-')
    photo_tag.short_description = 'Photo'


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'is_published', 'photo_tag']
    list_editable = ['is_published']
    list_display_links = ['id', 'title']

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width=80 height=auto>')
        else:
            return format_html('-')
    photo_tag.short_description = 'Photo'


admin.site.register(News, NewsAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.site_title = 'EvoTeam AdminPanel'
admin.site.site_header = 'EvoTeam AdminPanel'