# Generated by Django 3.1.3 on 2020-11-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20201111_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bean',
            name='price',
        ),
        migrations.AddField(
            model_name='bean',
            name='large_price',
            field=models.DecimalField(decimal_places=2, default=7.5, max_digits=6),
        ),
        migrations.AddField(
            model_name='bean',
            name='small_price',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=6),
        ),
        migrations.AlterField(
            model_name='bean',
            name='sizes',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
