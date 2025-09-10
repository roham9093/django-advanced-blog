from django.shortcuts import render

def indexView(request):
    return(request,'index.html')