from django.shortcuts import render
from mainApps.models import Posts, Attachments


def view_news(request):
    data = {'wall_content': Posts.objects.all()}
    return render(request, 'folders/main.html', context=data)


def view_contacts(request):
    return render(request, 'folders/contacts.html')
