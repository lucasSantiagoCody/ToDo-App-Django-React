from django.db import models
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _
from datetime import datetime
class ToDo(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('in_progress', _('In Progress')),
        ('completed', _('Completed')),
    ]

    PRIORYTY_CHOICES = [
        ('height', _('Height')),
        ('medium', _('Medium')),
        ('low', _('Low')),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    priority = models.CharField(max_length=6, choices=PRIORYTY_CHOICES)
    completed_at = models.DateField(null=True, blank=True)
    