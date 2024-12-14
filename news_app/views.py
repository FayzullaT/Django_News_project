from audioop import reverse
from lib2to3.fixes.fix_input import context
# from msilib.schema import ListView
from tkinter.font import names

from Tools.scripts.patchcheck import status
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from unicodedata import category

from .forms import ContactForm
from .models import News, Category, Contact

# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)
    # news_list = News.published.all()

    context = {
        "news_list" : news_list
    }
    return render(request, "news/news_list.html", context)

def news_detail(request, news):
    news=get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news":news
    }
    return render(request, 'news/news_detail.html', context)

def homePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:15]
    local_one = News.published.filter(category__name='Maxalliy').order_by("-publish_time")[:1]
    local_news = News.published.all().filter(category__name='Maxalliy').order_by("-publish_time")[1:6]
    context={
        'news_list':news_list,
        'categories':categories,
        'local_one':local_one,
        'local_news':local_news,
    }
    return render(request, 'news/index.html', context)

class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        context['news_list']=News.published.all().order_by('-publish_time')[:15]
        context['local_one']=News.published.filter(category__name='Maxalliy').order_by("-publish_time")[:1]
        context['local_news']=News.published.all().filter(category__name='Maxalliy').order_by("-publish_time")[1:6]
        context['out_one'] = News.published.filter(category__name='Xorij').order_by("-publish_time")[:1]
        context['out_news'] = News.published.all().filter(category__name='Xorij').order_by("-publish_time")[1:6]
        context['teh_one'] = News.published.filter(category__name='Texnologiya').order_by("-publish_time")[:1]
        context['teh_news'] = News.published.all().filter(category__name='Texnologiya').order_by("-publish_time")[1:6]
        context['sport_one'] = News.published.filter(category__name='Sport').order_by("-publish_time")[:1]
        context['sport_news'] = News.published.all().filter(category__name='Sport').order_by("-publish_time")[1:6]
        context['images'] =News.published.all().order_by('-publish_time')[:6]
        return context

# def contactPageView(request):
#     form = ContactForm(request.POST)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Biz bilan boglanganiz uchun raxmat!</h2>")
#
#     context = {
#         "form":form
#
#     }
#     return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form':form
        }
        return render(request, 'news/contact.html', context)
    def post(self, request):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan boglanganiz uchun raxmat!</h2>")
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

class LocalNewsList(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name = 'Maxalliy')
        return news

class XorijNewsList(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name = 'Xorij')
        return news

class TehnoNewsList(ListView):
    model = News
    template_name = 'news/tehno.html'
    context_object_name = 'tehno_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name = 'Texnologiya')
        return news

class SportNewsList(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name = 'Sport')
        return news

class NewsUpdateView(UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_edit.html'

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')

class NewsCreateView(CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug' , 'body', 'image', 'category', 'status')
