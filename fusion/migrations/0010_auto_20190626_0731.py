# Generated by Django 2.2.2 on 2019-06-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0009_auto_20190626_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='icons',
            field=models.CharField(choices=[('lni-rocket', 'rocket'), ('lni-laptop-phone', 'phone'), ('lni-cog', 'setting'), ('lni-leaf', 'leaf'), ('lni-layers', 'layers')], max_length=100),
        ),
        migrations.AlterField(
            model_name='featuresrght',
            name='icons',
            field=models.CharField(choices=[('lni-rocket', 'rocket'), ('lni-laptop-phone', 'phone'), ('lni-cog', 'setting'), ('lni-leaf', 'leaf'), ('lni-layers', 'layers')], max_length=100),
        ),
    ]
