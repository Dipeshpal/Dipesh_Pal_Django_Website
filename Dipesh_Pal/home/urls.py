from django.conf.urls import url

from . import views


app_name = 'home'


urlpatterns = [
    url(r'^$', views.homepage, name="list"),
    url(r'^News/', views.News, name="News"),
    url(r'^Android/', views.android, name="android"),
    url(r'^PC/', views.PC, name="PC"),
    url(r'^Others/', views.Others, name="Others"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/', views.article_update, name="post_edit"),
    url(r'^(?P<slug>[\w-]+)/delete/', views.article_delete, name="delete_post"),
]

