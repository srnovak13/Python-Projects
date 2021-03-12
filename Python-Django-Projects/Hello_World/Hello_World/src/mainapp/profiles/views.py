from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def display_name(request):
    userlist = UserProfile.objects.all()
    return render(request, "profiles/profiles_page.html", {'userlist': userlist})
