from django.conf.urls import url
from .views import search_filter

urlpatterns = [
    url(r'^$', search_filter, name='search')
    ]