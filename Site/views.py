from django.shortcuts import render


# Create your views here.
def index(request):

    return render(request, "Site/index.html")


def about(request):
    return render(request, "Site/about.html")


def services(request):
    return render(request, "Site/services.html")
