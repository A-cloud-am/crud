from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    data=Student.objects.all()
    return render(request,"home.html",{'data':data})

def delete_data(request,id):
    course=Student.objects.get(id=id)
    course.delete()
    return redirect('home')

def form_data(request):
    if request.method=="POST":
        data=request.POST
        name=data['name']
        email=data['email']
        contact=data['contact']
        message=data['message']
        var=Student(name=name,email=email,contact=contact,message=message)
        var.save()
        return HttpResponse("successfully submitted")
        
    return render(request,'form.html')


def edit(request,id):
    data=Student.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        message=request.POST['message']
        data=Student.objects.get(id=id)
        data.name=name
        data.email=email
        data.contact=contact
        data.message=message
     
          
        
        data.save()
        return redirect('home')
    return render(request,'edit.html',{'data':data})

    

