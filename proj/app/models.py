from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    pic = models.CharField(max_length=300)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
