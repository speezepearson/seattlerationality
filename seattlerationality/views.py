from django.shortcuts import render

def index(request):
  return render(request, 'seattlerationality/index.html',
                {'title': 'Seattle Rationality'})

def calendar(request):
  return render(request, 'seattlerationality/calendar.html',
                {'title': 'Calendar'})

def about(request):
  return render(request, 'seattlerationality/about.html',
                {'title': 'About'})

def contact(request):
  return render(request, 'seattlerationality/contact.html',
                {'title': 'Contact'})
