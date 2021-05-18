from django.contrib import admin
from mainApps.models import Posts, Attachments

@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    list_display = ['posting_date', 'post_id', 'text', 'main_history', 'author_name']


@admin.register(Attachments)
class AdminAttachmets(admin.ModelAdmin):
    list_display = ['type', 'url', 'preview', 'connect_post', 'height', 'width']
