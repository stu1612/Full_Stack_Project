{"filter":false,"title":"urls.py","tooltip":"/accounts/urls.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":7,"column":55},"end":{"row":7,"column":56},"action":"remove","lines":["n"],"id":2},{"start":{"row":7,"column":54},"end":{"row":7,"column":55},"action":"remove","lines":["o"]},{"start":{"row":7,"column":53},"end":{"row":7,"column":54},"action":"remove","lines":["i"]},{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"remove","lines":["t"]},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"remove","lines":["a"]},{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"remove","lines":["r"]}],[{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"insert","lines":["e"],"id":3},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":60},"end":{"row":1,"column":61},"action":"remove","lines":["n"],"id":4},{"start":{"row":1,"column":59},"end":{"row":1,"column":60},"action":"remove","lines":["o"]},{"start":{"row":1,"column":58},"end":{"row":1,"column":59},"action":"remove","lines":["i"]},{"start":{"row":1,"column":57},"end":{"row":1,"column":58},"action":"remove","lines":["t"]},{"start":{"row":1,"column":56},"end":{"row":1,"column":57},"action":"remove","lines":["a"]},{"start":{"row":1,"column":55},"end":{"row":1,"column":56},"action":"remove","lines":["r"]}],[{"start":{"row":1,"column":55},"end":{"row":1,"column":56},"action":"insert","lines":["e"],"id":5},{"start":{"row":1,"column":56},"end":{"row":1,"column":57},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":["from django.conf.urls import url, include","from accounts.views import index, logout, login, register, user_profile","from accounts import url_reset","","urlpatterns = [","    url(r'^logout/$', logout, name=\"logout\"),","    url(r'^login/$', login, name=\"login\"),","    url(r'^register/$', registration, name=\"register\"),","    url(r'^profile/$', user_profile, name=\"profile\"),","    url(r'^password_reset/', include(url_reset))","]"],"id":6},{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from . import urls_reset","from .views import index, register, profile, logout, login","","urlpatterns = [","    url(r'^register/$', register, name='register'),","    url(r'^profile/$', profile, name='profile'),","    url(r'^logout/$', logout, name='logout'),","    url(r'^login/$', login, name='login'),","    url(r'^password-reset/', include(urls_reset)),","]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":0},"end":{"row":11,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1570706510354,"hash":"24d9562b3f60b7c396c136f09c625abe655faab0"}