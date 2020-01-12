from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import JSONField, Model

class Chat(Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    chat_ans = JSONField()

    def __str__(self):
        return self.question

