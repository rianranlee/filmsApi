from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=127, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(auto_now_add=True, editable=False)