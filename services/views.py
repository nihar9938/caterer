from django.shortcuts import render
from .models import *
# Create your views here.
def Front(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        Type = request.POST['Type']
        obj = Contact(Name=Name,Phone=Phone,Type=Type,Email=Email)
        obj.save()
    return render(request,'index.html')

