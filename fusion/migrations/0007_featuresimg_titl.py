# Generated by Django 2.2.2 on 2019-06-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0006_auto_20190626_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuresimg',
            name='Titl',
            field=models.CharField(default=1, help_text='Enter Tittle', max_length=20),
            preserve_default=False,
        ),
    ]