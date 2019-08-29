# Generated by Django 2.2.2 on 2019-06-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0008_featuresrght'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='icons',
            field=models.CharField(choices=[('fa fa-cog', 'settings'), ('fa fa-line-chart', 'design'), ('fa fa-user', 'customize'), ('fa fa-align-justify', 'ui'), ('fa fa-android', 'app'), ('fa fa-sign-language', 'ufrnd')], max_length=100),
        ),
        migrations.AlterField(
            model_name='featuresrght',
            name='icons',
            field=models.CharField(choices=[('fa fa-cog', 'settings'), ('fa fa-line-chart', 'design'), ('fa fa-user', 'customize'), ('fa fa-align-justify', 'ui'), ('fa fa-android', 'app'), ('fa fa-sign-language', 'ufrnd')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='icons2',
            field=models.CharField(choices=[('fa fa-rocket', 'pro'), ('fa fa-star-half-o', 'plus'), ('fa fa-star-o', 'primium')], max_length=100),
        ),
        migrations.AlterField(
            model_name='services',
            name='icons',
            field=models.CharField(choices=[('fa fa-cog', 'settings'), ('fa fa-line-chart', 'design'), ('fa fa-user', 'customize'), ('fa fa-align-justify', 'ui'), ('fa fa-android', 'app'), ('fa fa-sign-language', 'ufrnd')], max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='icons1',
            field=models.CharField(choices=[('fa fa-instagram', 'insta'), ('fa fa-facebook', 'facebook'), ('fa fa-twitter', 'twitter')], max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='icons11',
            field=models.CharField(choices=[('fa fa-instagram', 'insta'), ('fa fa-facebook', 'facebook'), ('fa fa-twitter', 'twitter')], max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='icons12',
            field=models.CharField(choices=[('fa fa-instagram', 'insta'), ('fa fa-facebook', 'facebook'), ('fa fa-twitter', 'twitter')], max_length=200),
        ),
    ]
