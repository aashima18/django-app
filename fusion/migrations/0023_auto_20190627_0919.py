# Generated by Django 2.2.2 on 2019-06-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0022_auto_20190627_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]