from django.shortcuts import render
from myweb.models import Contact
# Create your views here.

def home_view(request):
  return render(request, "website/index.html")

def about_view(request):
  return render(request, "website/about.html")

def contact_view(request):
  return render(request, "website/contact.html")

def elements_view(request):
  return render(request, "website/elements.html")

def test_forms(request):
  if request.method == "POST":
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")
    c = Contact()
    c.name = name
    c.email = email
    c.subject = subject
    c.message = message
    c.save()
    print(name , email , message , subject)
  return render(request,"test-forms.html")