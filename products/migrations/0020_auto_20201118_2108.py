# Generated by Django 3.1.3 on 2020-11-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20201118_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bean',
            name='image',
        ),
        migrations.AddField(
            model_name='country',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]
