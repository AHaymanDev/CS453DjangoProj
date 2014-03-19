from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static

from bookrental import views

urlpatterns = patterns('',
     url(r'^$', 'bookrental.views.login', name=u"login"), # first webpage
     url(r'^book/$', 'bookrental.views.book', name=u"book"),
     url(r'^checkout/$', 'bookrental.views.checkout', name=u"checkout"),
     url(r'^info/$', 'bookrental.views.info', name=u"info"),
     url(r'^return_confirm/$', 'bookrental.views.return_confirm', name=u"return_confirm"),
     url(r'^returns/$', 'bookrental.views.returns', name=u"returns"),
     url(r'^warning/$', 'bookrental.views.warning', name=u"warning"),
     url(r'^cart/$', 'bookrental.views.cart', name=u"cart"),
     url(r'^category/$', 'bookrental.views.category', name=u"category"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)