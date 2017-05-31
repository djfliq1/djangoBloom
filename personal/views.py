from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['Please email Clarence Hairston:', 'djfliq1@gmail.com']})

def ellis(request):
    return render(request, 'personal/ellis.html')
