from django.db import models

class Quote(models.Model):
    def __str__(self):
        return self.quote_text
    quote_text = models.CharField(max_length=200)