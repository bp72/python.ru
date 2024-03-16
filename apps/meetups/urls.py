from django.urls import path

from . import views


urlpatterns = [
    path(r'^(?P<event_slug>\w+)/$', views.EventDetailView.as_view(), name='event_detail_view'),
]
