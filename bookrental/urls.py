from django.conf.urls import patterns, url, include

from polls import views

urlpatterns = patterns('',
     url(r'^$', views.cart, name='cart')
)