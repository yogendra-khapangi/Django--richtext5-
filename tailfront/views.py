from django.shortcuts import render

# Create your views here.
def index(request):
    print("hello world")
    return render(request,'tailfront/index.html')

def about(request):
    return render(request,"/about.html")