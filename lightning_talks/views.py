from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  # Adapted from https://docs.djangoproject.com/en/1.9/intro/tutorial03/#a-shortcut-render
  return render(request, 'lightning_talks/index.html', {'all_talks': ['a', 'b', 'c']})
