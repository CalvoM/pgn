from django.shortcuts import render


def home(request):
    return render(request, "past_chess/index.html")


# Create your views here.
