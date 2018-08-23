from django.conf.urls import url
from django.contrib import admin
from . import views

# r is for raw string 
# ^ means anything before hand has to match 
# the $ means it needs to end like that
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
]