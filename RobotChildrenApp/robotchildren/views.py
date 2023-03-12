from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def create(request):
    # template = loader.get_template('robotchildren/login.html')
    # context = {"wtf":"Wtf"}
    # return HttpResponse(template.render(context, request))
    return render(request, "robotchildren/index.html")
def textloop(request):
    template = loader.get_template('robotchildren/textloop.html')
    context = {"wtf":"Wtf"}
    return HttpResponse(template.render(context, request))

# Create your views here.
