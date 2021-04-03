from django.db import models
#mdel Contact-> Getinfo  name-> hashtag email-> tweetcount
# Create your models here.
class Getinfo(models.Model):
    hashtag=models.CharField(max_length=200)
    tweetcount= models.CharField(max_length=100)
    def _str_(self):
        return self.hashtag