from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=220 ,null=False , blank=False)
    email = models.EmailField(max_length=220 ,null=False , blank=False)
    contact = models.IntegerField(null=False , blank=False)
    messages = models.TextField(null=False , blank=False)
    
    def __str__(self):
        return "{0} - {1}".format(self.name, self.email)




