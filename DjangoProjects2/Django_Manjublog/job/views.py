from django.shortcuts import render
from .models import Job


def index(request):
    works = Job.objects.all()
    return render(request, 'job/home.html', {'works': works})
