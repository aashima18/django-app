# Generated by Django 2.2.2 on 2019-06-25 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0002_auto_20190625_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='icons',
            field=models.CharField(choices=[('settings', 'fa fa-cog'), ('design', 'fa fa-line-chart'), ('customize', 'fa fa-user'), ('ui', 'fa fa-align-justify'), ('app', 'fa fa-android'), ('ufrnd', 'fa fa-sign-language')], max_length=1),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='icons2',
            field=models.CharField(choices=[('pro', 'fa fa-rocket'), ('plus', 'fa fa-star-half-o'), ('primium', 'fa fa-star-o')], max_length=1),
        ),
        migrations.AlterField(
            model_name='team',
            name='icons1',
            field=models.CharField(choices=[('insta', 'fa fa-instagram'), ('facebook', 'fa fa-facebook'), ('twitter', 'fa fa-twitter')], max_length=1),
        ),
    ]
