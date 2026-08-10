from django.db import models
from django.utils import timezone


class EmailNotification(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.recipient_email} - {self.subject}"
    
class LogEntry(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.created_at} - {self.message[:50]}"
    
class ScrapedPage(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    scraped_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.url}"
    
class UploadedImage(models.Model):
    image = models.ImageField(upload_to="uploaded_images/")
    classification_result = models.CharField(
        max_length=255,
        blank=True,
    )

    def __str__(self):
        return f"Image {self.id}"

class TransactionItem(models.Model):
    name = models.CharField(max_length=255)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.name