from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Notification, User

    
# Create your views here.
def all_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, "quote.html", {"notifications": notifications})    
