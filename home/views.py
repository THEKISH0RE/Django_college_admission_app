from django.shortcuts import render, HttpResponse
from home.models import Register

# Create your views here.

def home(request):
  # return HttpResponse("this is my home page ")
  return render(request, 'home.html')
def contact(request):
  return render(request, 'contact.html')
  # return HttpResponse("this is my contact page ")

def about(request):
  return render(request, 'about.html')
  # return HttpResponse("this is my contact page ")
def form(request):
  # if request.method=="POST":
  #   name = request.POST['name']
  #   phone = request.POST['phone']
  #   email = request.POST['email']
  #   group = request.POST['group']
  #   college = request.POST['college']

  #   ins = Register(name=name, phone=phone, email=email, group=group, college=college)
  #   ins.save()

  #   print("The data has been written to the DB")
  return render(request, 'form.html')

def final(request):
  if request.method=="POST":
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    group = request.POST['group']
    college = request.POST['college']

    ins = Register(name=name, phone=phone, email=email, group=group, college=college)
    ins.save()
    print("The data has been written to the DB")
  return render(request, 'final.html')


