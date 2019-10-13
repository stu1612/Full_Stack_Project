from django.conf.urls import url, include
from .views import all_notifications

urlpatterns = [
    url(r'^$', all_notifications, name='notifications'),
]