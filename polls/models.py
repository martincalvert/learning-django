import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
  def __unicode__(self):
    return "{} {}".format(self.id, self.question_text)

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  def __unicode__(self):
    return "{} {}".format(self.id, self.question_text)
  choice_text = models.CharField(max_length=200)
  question = models.ForeignKey(Question)
  votes = models.IntegerField(default=0)
