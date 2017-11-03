from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dict = {'insert_me': "Hello i am from Views.py"}
    return render(request, 'account_sign/index.html', context=my_dict)
