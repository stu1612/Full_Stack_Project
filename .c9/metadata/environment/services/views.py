{"filter":false,"title":"views.py","tooltip":"/services/views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here."],"id":2},{"start":{"row":0,"column":0},"end":{"row":6,"column":67},"action":"insert","lines":["from django.shortcuts import render","from .models import Service","","# Create your views here.","def all_services(request):","    services = Service.objects.all()","    return render(request, \"services.html\", {\"services\": services})"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":0},"end":{"row":7,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1570878795824,"hash":"682332c3b334893a460224bc6fb3ee116839140d"}