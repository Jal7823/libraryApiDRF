# Generated by Django 4.1.4 on 2022-12-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='book',
            field=models.ManyToManyField(blank=True, null=True, related_name='Libro', to='books.books'),
        ),
        migrations.AlterField(
            model_name='library',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Photo'),
        ),
    ]
