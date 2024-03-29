# Generated by Django 2.2.2 on 2019-06-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0004_auto_20190625_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='icons11',
            field=models.CharField(choices=[('insta', 'fa fa-instagram'), ('facebook', 'fa fa-facebook'), ('twitter', 'fa fa-twitter')], default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='icons12',
            field=models.CharField(choices=[('insta', 'fa fa-instagram'), ('facebook', 'fa fa-facebook'), ('twitter', 'fa fa-twitter')], default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='Tittle',
            field=models.CharField(help_text='Enter Tittle', max_length=200),
        ),
        migrations.AlterField(
            model_name='services',
            name='icons',
            field=models.CharField(choices=[('settings', 'fa fa-cog'), ('design', 'fa fa-line-chart'), ('customize', 'fa fa-user'), ('ui', 'fa fa-align-justify'), ('app', 'fa fa-android'), ('ufrnd', 'fa fa-sign-language')], max_length=100),
        ),
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(help_text='Enter heading', max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='Title1',
            field=models.CharField(help_text='Enter Tittle', max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='icons1',
            field=models.CharField(choices=[('insta', 'fa fa-instagram'), ('facebook', 'fa fa-facebook'), ('twitter', 'fa fa-twitter')], max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='name1',
            field=models.CharField(help_text='Enter Tittle', max_length=200),
        ),
    ]
