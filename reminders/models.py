from django.db import models

# Create your models here.
from django.db import models

class Reminder(models.Model):
    REMINDER_TYPE = [
        ('SMS', 'SMS'),
        ('Email', 'Email'),
    ]
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_TYPE)