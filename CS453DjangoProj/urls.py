from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CS453DjangoProj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#r'^$' needs to be r'^bookrental/' from my understanding because without that part there is no
#way to get to the other pages.
#Example if you put /book/ or /bookrental/book/ there is no match here for that
    url(r'^$', include('bookrental.urls')),
    #url(r'^bookrental/', include('bookrental.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
