from django.conf import settings
from django.urls import path, re_path
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apps.news import views as news_views


urlpatterns = [
    re_path(r'^$', news_views.IndexView.as_view(), name='index'),
    re_path(r'^meetups/', include('apps.meetups.urls')),
    re_path(r'^junior/$', news_views.JuniorView.as_view(), name='junior'),
    re_path(r'^post/(?P<pk>\d+)/$', news_views.PostView.as_view(), name='post_page'),

    re_path(r'^admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()