from django.db import models

# Create your models here.


class Urls(models.Model):
    short_id = models.CharField(max_length=250)
    httpurl = models.URLField(max_length=250)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.httpurl
