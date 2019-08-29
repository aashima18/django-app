# Generated by Django 2.2.2 on 2019-06-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0010_auto_20190626_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='icons2',
            field=models.CharField(choices=[('fa fa-instagram', 'insta'), ('lni-facebook-filled', 'facebook'), ('lni-instagram-filled', 'twitter')], max_length=100),
        ),
        migrations.AlterField(
            model_name='services',
            name='icons',
            field=models.CharField(choices=[('lni-cog', 'settings'), ('lni-stats-up', 'design'), ('lni-users', 'customize'), ('lni-layers', 'ui'), ('lni-mobile', 'app'), ('lni-rocket', 'ufrnd')], max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='icons1',
            field=models.CharField(choices=[('fa fa-instagram', 'insta'), ('lni-facebook-filled', 'facebook'), ('lni-instagram-filled', 'twitter')], max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='icons11',
            field=models.CharField(choices=[('fa fa-instagram', 'insta'), ('lni-facebook-filled', 'facebook'), ('lni-instagram-filled', 'twitter')], max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='icons12',
            field=models.CharField(choices=[('fa fa-instagram', 'insta'), ('lni-facebook-filled', 'facebook'), ('lni-instagram-filled', 'twitter')], max_length=200),
        ),
    ]
