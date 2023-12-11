from django.shortcuts import render, redirect
from myapp.models import Course
from myapp.forms import updateForm

# Create your views here.
def home(req):
    data = Course.objects.all()
    return render(req, 'myapp/home.html', {'data': data})

def update(req, id):
    data = Course.objects.get(pk=id)
    form = updateForm(instance=data)
    if req.method == "POST":
        form = updateForm(req.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(req, 'myapp/update.html', {'form':form, 'id':id})