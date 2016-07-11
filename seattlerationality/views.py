from django.shortcuts import render

def index(request):
  return render(request, 'seattlerationality/index.html',
                {'title': 'Seattle Rationality'})

def calendar(request):
  return render(request, 'seattlerationality/calendar.html',
                {'title': 'Calendar'})
