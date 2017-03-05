# -*- coding: utf-8 -*-

"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from article.models import Article
from article.views import home,detail,archives,about_me,search_tag,blog_search,RSSFeed
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name ='home'),
    url(r'^(?P<id>\d+)/$',detail, name ='detail'),
    url(r'^archives/$',archives,name='archives'),
    url(r'^aboutme/$',about_me,name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', search_tag, name = 'search_tag'),
    url(r'^search/$', blog_search,name='search'),
    url(r'^feed/$', RSSFeed(), name = "RSS"), 
    {'document_root', settings.STATIC_ROOT},
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
