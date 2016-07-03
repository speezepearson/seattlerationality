import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'seattlerationality.settings'

import django
django.setup()

import datetime as dt
from lightning_talks.models import LightningTalk as LT

LT(
  speaker='Spencer', title='Making a SeaRat site With Django',
  given_on=dt.date(2016, 7, 2),
  embed_video_html='<iframe width="560" height="315" src="https://www.youtube.com/embed/qgGIqRFvFFk?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK" frameborder="0" allowfullscreen></iframe>').save()

LT(
  speaker='eHarmony Girl', title='Cats',
  given_on=dt.date(2016, 1, 1),
  embed_video_html='<iframe width="420" height="315" src="https://www.youtube.com/embed/sP4NMoJcFd4" frameborder="0" allowfullscreen></iframe>').save()
