from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from myweb.models import Contact
from myweb.forms import NameForm , ContactForm , NewsletterForm
from django.contrib import messages
# Create your views here.

def home_view(request):
  return render(request, "website/index.html")

def about_view(request):
  return render(request, "website/about.html")

def contact_view(request):
    if request.method == "POST":
      form = ContactForm(request.POST)
      if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"your ticket submited successfully!")
      else:
        messages.add_message(request,messages.ERROR,"your didnt ticket submited successfully")
    form = ContactForm()
    return render(request, "website/contact.html", {'form':form})

def newsletter_view(request):
  if request.method == "POST":
    form = NewsletterForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/")
  else:
    return HttpResponseRedirect("/")
def elements_view(request):
  return render(request, "website/elements.html")

# # method 1:just using view
# def test_forms(request):
#   if request.method == "POST":
#     name = request.POST.get("name")
#     email = request.POST.get("email")
#     subject = request.POST.get("subject")
#     message = request.POST.get("message")
#     c = Contact()
#     c.name = name
#     c.email = email
#     c.subject = subject
#     c.message = message
#     c.save()
#     print(name , email , message , subject)
#   return render(request,"test-forms.html")

## method 2: using django forms for forms without connection to models
# def test_forms(request):
#   if request.method == "POST":
#     form = NameForm(request.POST)
#     if form.is_valid():
#       name = form.cleaned_data["name"]
#       email = form.cleaned_data["email"]
#       subject = form.cleaned_data["subject"]
#       message = form.cleaned_data["message"]
#       print(name , email , subject , message)
#       return HttpResponse("done")
#     else:
#       return HttpResponse("not valid")
#   form = NameForm()
#   return render(request,"test-forms.html", {'form':form})

## method 3: using model forms for forms with connection to models
def test_forms(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse("done")
    else:
      return HttpResponse("not valid")
  form = ContactForm()
  return render(request,"test-forms.html", {'form':form})
