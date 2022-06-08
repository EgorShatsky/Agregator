from django.db import models
from django.urls import reverse


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(max_length=255)
    cost = models.IntegerField(max_length=255)
    phone = models.IntegerField(max_length=11)
    mail = models.CharField(max_length=255)
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,
                            null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
