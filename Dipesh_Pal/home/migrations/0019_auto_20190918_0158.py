# Generated by Django 2.2.5 on 2019-09-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_home_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='category',
            field=models.CharField(choices=[('NEWS', 'News'), ('ANDROID', 'Android'), ('PC', 'PC'), ('OTHERS', 'Others')], default='OTHERS', max_length=2),
        ),
    ]
