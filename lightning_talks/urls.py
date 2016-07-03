# Adapted from https://docs.djangoproject.com/en/1.9/intro/tutorial01/#write-your-first-view

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /lightning_talks/
    url(r'^$', views.index, name='index')
]
