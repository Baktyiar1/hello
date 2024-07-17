from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.name

class Hello(models.Model):
    title = models.CharField(max_length=100)
    descrption = models.TextField()
    price = models.DecimalField(max_digits=15,decimal_places=2)
    people = models.ForeignKey(Person,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/image')
    video = models.FileField(upload_to='media/video')

    def __str__(self):
        return self.title

