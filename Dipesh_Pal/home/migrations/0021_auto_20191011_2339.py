# Generated by Django 2.2.5 on 2019-10-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20190920_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='category',
            field=models.CharField(choices=[('NEWS', 'News'), ('ANDROID', 'Android'), ('PC', 'PC'), ('OFFERS', 'Offers'), ('OTHERS', 'Others')], default='OTHERS', max_length=20),
        ),
    ]
