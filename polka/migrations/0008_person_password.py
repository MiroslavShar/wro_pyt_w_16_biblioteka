# Generated by Django 4.2.7 on 2023-12-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polka', '0007_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='qwerty', max_length=64),
        ),
    ]
