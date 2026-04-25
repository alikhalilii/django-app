from django.http import HttpResponse , JsonResponse

def http_test(request):
  return HttpResponse("<h1>Hi This is a test</h1>")

def json_test(request):
  return JsonResponse({"name":"ali" , "last name":"khalili"})