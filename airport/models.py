from django.db import models

# Create your models here.
class airports_city(models.Model):
    airport_name=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    website_link=models.TextField()
    weather_href=models.TextField()
    weather_pics_link=models.TextField()
    def __str__(self):
        return self.airport_name


class airport_img(models.Model):
    img_link=models.TextField()
    city=models.CharField(max_length=250)
    def __str__(self):
        return self.city

class airport_fact(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    city=models.CharField(max_length=250)


    def __str__(self):
        return self.city
