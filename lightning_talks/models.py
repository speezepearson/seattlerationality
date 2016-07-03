from django.db import models

# Create your models here.

# adapted from https://docs.djangoproject.com/en/1.9/intro/tutorial02/#creating-models
class LightningTalk(models.Model):
  title = models.CharField(max_length=255, unique=True)
  speaker = models.CharField(max_length=255)
  given_on = models.DateTimeField('date given')
  embed_video_html = models.CharField(max_length=4095)

  def __str__(self):
    return '<LightningTalk given by {speaker} on {date:%Y-%m-%d} about {title!r}>'.format(
      speaker=self.speaker,
      date=self.given_on,
      title=self.title)
