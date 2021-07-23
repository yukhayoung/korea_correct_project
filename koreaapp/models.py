from django.db import models

# Create your models here.
class Koreaapp(models.Model):      #class상속을받는다.
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="koreaapp/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:5] 