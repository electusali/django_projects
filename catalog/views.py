from django.shortcuts import render,HttpResponse

# Create your views here.
def veri(request):
    return HttpResponse('<h1> Merhaba </h1>')
