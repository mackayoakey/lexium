from django.db import models

class TextResource(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True) # For storing text directly
    uploaded_file = models.FileField(upload_to='uploaded_texts/', blank=True, null=True)  # For file uploads
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title