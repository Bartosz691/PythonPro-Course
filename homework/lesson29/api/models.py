from django.db import models


class EmailNotification(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.recipient_email} - {self.subject}"