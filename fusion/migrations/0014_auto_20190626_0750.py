# Generated by Django 2.2.2 on 2019-06-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0013_auto_20190626_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='icons1',
            field=models.CharField(choices=[('lni-instagram-filled', 'insta'), ('lni-facebook-filled', 'facebook'), ('lni-instagram-filled', 'twitter')], max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='icons12',
            field=models.CharField(choices=[('lni-instagram-filled', 'insta'), ('lni-facebook-filled', 'facebook'), ('lni-instagram-filled', 'twitter')], max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='icons13',
            field=models.CharField(choices=[('lni-instagram-filled', 'insta'), ('lni-facebook-filled', 'facebook'), ('lni-instagram-filled', 'twitter')], max_length=200),
        ),
    ]
