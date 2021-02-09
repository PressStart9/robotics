from django.shortcuts import render
from mainApps.models import Posts, Attachments
from django.db.models import Q
from  el_pagination.decorators  import  page_template

@page_template('folders/news_list_page.html')
def view_invents(request, template='folders/news.html', page_template='folders/news_list_page.html', extra_context=None):
    print(Posts.objects.filter(text__icontains='пригла').all())
    context = {
        'wall_content': Posts.objects.filter(text__icontains='пригла'),
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)

def view_schedule(request):
    data = {'wall_content': Posts.objects.filter(Q(text__icontains='расписани') & Q(text__icontains='на'))}
    return render(request, 'folders/schedule.html', context=data)

def view_main(request):
    return render(request, 'folders/contacts.html')

@page_template('folders/news_list_page.html')
def view_news(request, template='folders/news.html', page_template='folders/news_list_page.html', extra_context=None):
    context = {
        'wall_content': Posts.objects.all(),
        'page_template': page_template,
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)
