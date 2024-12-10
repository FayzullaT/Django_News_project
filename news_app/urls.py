from tkinter.font import names

from django.urls import path

# from news_project.urls import urlpatterns
from .views import news_list, news_detail, homePageView, ContactPageView, HomePageView, \
    LocalNewsList, XorijNewsList, TehnoNewsList, SportNewsList

urlpatterns = [
    # path('', homePageView, name = 'home_page'),
    path('', HomePageView.as_view(), name = 'home_page'),
    path('news/', news_list, name = 'all_news_list'),
    path('news/<slug:news>/', news_detail, name = 'news_detail_page'),
    path('contact_us', ContactPageView.as_view(), name = 'contact_page'),
    path('local-news/', LocalNewsList.as_view(), name='local_news_page'),
    path('xorij-news/', XorijNewsList.as_view(), name='xorij_news_page'),
    path('tehno-news/', TehnoNewsList.as_view(), name='tehno_news_page'),
    path('sport-news/', SportNewsList.as_view(), name='sport_news_page'),
]