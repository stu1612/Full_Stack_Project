from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, profile, logout, login, review, add_review

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^review/$', review, name='review'),
    url(r'^review/add$', add_review, name='add_review'),
]
