# Generated by Django 2.2.2 on 2019-07-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorymanagement', '0010_auto_20190702_0728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AddField(
            model_name='category',
            name='summary',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]