from django.db import models
from start.models import Start

# Create your models here.
class Complete(models.Model):
    start = models.ForeignKey(Start, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    complete_timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body
    
    class Meta:
        ordering = ('-complete_timestamp',)
        verbose_name = ("Complete")
        verbose_name_plural = ("Completes")
    