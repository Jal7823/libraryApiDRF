from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Author'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

class Editorial(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Editorial'
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editorials'

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Books(models.Model):
    name = models.CharField('Nombre',max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='Autor')
    price = models.DecimalField('Precio',max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='Categoria')
    editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE,related_name='Editorial')
    image = models.ImageField(upload_to='frontPage')
    publication = models.IntegerField(default=1800)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Books'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    