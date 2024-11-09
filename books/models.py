from django.db import models

class Bok(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.Datefield()
    def __str__(self):
        return self.title