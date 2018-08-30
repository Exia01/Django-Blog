from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from articles import views as article_views

from . import views

# r is for raw string
# ^ means anything before hand has to match
# the $ means it needs to end like that
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',article_views.article_list, name='home'),

    # Apps
    url(r'^accounts/', include('accounts.urls')),
    url(r'^articles/', include('articles.urls')), # routes will be added to it later so we don't need the dollar sign
    url(r'^about/$', views.about),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
