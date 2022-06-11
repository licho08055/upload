from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=60)
    document=models.FileField(upload_to='documents/')
    
    class Meta:
        ordering=['title']
    
    
    def __str__(self):
        return self.title
