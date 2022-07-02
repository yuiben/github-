import imp
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    myname = "ben bùi"
    hangXe = ["yamaha","honda","suzuki"]
    context = {"name": myname,"thuonghieu":hangXe}
    return render(request, "polls/index.html", context)