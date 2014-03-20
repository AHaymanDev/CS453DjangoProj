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
     url(r'^login_failure/$', 'bookrental.views.login_failure', name=u"login_failure"),
     url(r'^new_user/$', 'bookrental.views.new_user', name=u"new_user"),
     url(r'^update_user/$', 'bookrental.views.update_user', name=u"update_user"),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
