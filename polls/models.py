import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
  def __unicode__(self):
    return "{} {}".format(self.id, self.question_text)

  def was_published_recently(self):
    return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  def __unicode__(self):
    return "{} {}".format(self.id, self.choice_text)
  choice_text = models.CharField(max_length=200)
  question = models.ForeignKey(Question)
  votes = models.IntegerField(default=0)
