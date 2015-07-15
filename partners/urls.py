from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^lost/$', views.lost_item, name='lost_item'),
    url(r'^found/$', views.found_item, name='found_item'),
    url(r'^found/pickup/$', views.found_item_confirmed, name='found_item_confirmed'),
    url(r'^partners/$', views.partners, name='partners'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^privacy/$', views.privacy, name='privacy'),
]