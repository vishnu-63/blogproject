# Generated by Django 3.2.6 on 2021-08-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='nopic.png', upload_to='bigimg'),
        ),
    ]
