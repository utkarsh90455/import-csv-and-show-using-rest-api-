from django.db import models

# Create your models here.
class csvData(models.Model):
    Message=models.CharField(max_length=200)
    truth=models.CharField(max_length=200)
    cube=models.CharField(max_length=200)
    google=models.CharField(max_length=200)
    google_spam=models.FloatField(max_length=200)
    google_not_spam=models.FloatField(max_length=200)
    ibm=models.CharField(max_length=200)
    ibm_spam=models.FloatField(max_length=200)
    ibm_not_spam=models.FloatField(max_length=200)

    def __str__(self):
        return self.Message

