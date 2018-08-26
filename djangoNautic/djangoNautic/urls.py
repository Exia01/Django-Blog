from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# r is for raw string 
# ^ means anything before hand has to match 
# the $ means it needs to end like that
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')), # things will be added to it later so we don't need the dollar sign
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
]
urlpatterns += staticfiles_urlpatterns()