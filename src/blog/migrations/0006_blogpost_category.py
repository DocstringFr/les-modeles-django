# Generated by Django 3.1.6 on 2021-02-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]