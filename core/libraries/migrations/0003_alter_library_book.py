# Generated by Django 4.1.4 on 2022-12-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('libraries', '0002_alter_library_book_alter_library_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='book',
            field=models.ManyToManyField(related_name='Libro', to='books.books'),
        ),
    ]
