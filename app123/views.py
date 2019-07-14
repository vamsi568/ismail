from django.shortcuts import render

# Create your views here.

def ShowIndex(request):
    return render(request,"index.html")


def Video(request):
    return render(request,"showindex.html")

"""

def Democreamapp(request):
    return render(request,"demo-cream-app.html")    
    



def Demoimagebackground(request):
    return render(request,"demo-image-background.html")


def Demorestaurant(request):
    return render(request,"demo-restaurant.html")

def Demovideobackground(request):
    return render(request,"demo-video-background.html")    
    
"""    