from django.shortcuts import render
from .models import Resource, Exam

def home(request):
    return render(request, 'cbresources/home.html', {})

def about(request):
    return render(request, 'cbresources/about.html', {})

def ap(request):
    aps = Exam.objects.filter(testType__exact='ap').order_by('name')
    return render(request, 'cbresources/ap.html', {
        'aps': aps
    })

def sat(request):
    sats = Exam.objects.filter(testType__exact='sat').order_by('name')
    return render(request, 'cbresources/sat.html', {
        'sats': sats
    })

def goTest(request, testName):
    resources = Resource.objects.filter(testName__exact=testName).order_by('link')
    return render(request, 'cbresources/sources.html', {
        'resources': resources
    })