from django.db import models
from django.utils import timezone
import uuid

class Sub(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    subed_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email

class Newsletter(models.Model):
    body = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)
    was_sent = models.BooleanField(default=False)
    subject = models.CharField(max_length=250)
    newsletter_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.subject

class SentNewsletter(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    sub = models.ForeignKey(Sub, on_delete=models.CASCADE)
    sent_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[('sent', 'Sent',), ('failed', 'Failed')])

    def __str__(self):
        return f'{self.newsletter.subject} to {self.sub.email}'


    
