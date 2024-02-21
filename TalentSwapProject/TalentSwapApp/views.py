from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   # return HttpResponse('Welcome to TalentSwap') (Tutorial)
    return render(request, 'TalentSwapApp/home.html') # Home de verdad

def about(request):
    return HttpResponse('About TalentSwap')
