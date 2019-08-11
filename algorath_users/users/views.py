from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome! You are at our Users app.")

