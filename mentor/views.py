from django.shortcuts import render
from .models import mentor_detail

def home(request):
    context = {
        'mentors' : mentor_detail.objects.all()
    }
    return render(request, 'mentor/mentor.html', context)
