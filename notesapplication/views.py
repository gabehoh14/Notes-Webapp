from django.shortcuts import render

# Create your views here.
def take_notes(request):
    return render(request, "notes.html")