# Generated by Django 2.1.7 on 2019-02-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190226_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='slug',
            field=models.SlugField(default=511),
        ),
    ]
