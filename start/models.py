from django.db import models

# Create your models here.
class Start(models.Model):
    title = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-timestamp',)
        verbose_name = ("Start")
        verbose_name_plural = ("Starts")
    
