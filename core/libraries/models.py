from django.db import models
from core.books.models import Books

class Library(models.Model):
    name = models.CharField('Nombre', max_length=50)
    address = models.CharField('Direcccion',max_length=50)
    book = models.ManyToManyField(Books,related_name='Libro')
    image = models.ImageField(upload_to='Photo',null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Library'
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'