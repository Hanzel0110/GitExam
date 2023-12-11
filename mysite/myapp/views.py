from django.shortcuts import render, redirect
from myapp.models import Course

# Create your views here.
def home(req):
    data = Course.objects.all()
    return render(req, 'myapp/home.html', {'data': data})