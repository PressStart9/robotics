from django.contrib import admin
from mainApps.models import Posts, Attachments


@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    list_display = ['posting_date', 'post_id', 'text']
    search_fields = ['text']


@admin.register(Attachments)
class AdminAttachmets(admin.ModelAdmin):
    list_display = ['type', 'url']
    search_fields = ['text']
