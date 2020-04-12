from django.db import models
from django.utils import timezone

# Create your models here.
class ChatLog(models.Model):
    sendId = models.IntegerField(null=False, blank=False)
    recvId = models.IntegerField(null=False, blank=False)
    message = models.TextField(null=False)
    sendTime = models.DateTimeField(default=timezone.now, null=False, blank=False)
