# Generated by Django 2.2.2 on 2019-07-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorymanagement', '0003_auto_20190701_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
