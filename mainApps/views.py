from django.shortcuts import render
from mainApps.models import Posts, Attachments
from django.db.models import Q

def view_main(request):
    data = {'wall_content': Posts.objects.filter((Q(text__icontains='пригла') & Q(text__icontains='участ')) | (Q(text__icontains='расписание') & Q(text__icontains='год'))).all()}
    return render(request, 'folders/news.html', context=data)


def view_news(request):
    data = {'wall_content': Posts.objects.all()}
    return render(request, 'folders/news.html', context=data)


def view_contacts(request):
    return render(request, 'folders/contacts.html')
