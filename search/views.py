from django.shortcuts import render
from services.models import Service

# Create your views here.

def search_filter(request):
    services = Service.objects.filter(title__icontains=request.GET['q'])
    return render(request, "services.html", {"services":services})
