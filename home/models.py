from django.db import models
from django.utils.timezone import now
# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email
