# Generated by Django 2.2.2 on 2019-07-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorymanagement', '0002_auto_20190701_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
