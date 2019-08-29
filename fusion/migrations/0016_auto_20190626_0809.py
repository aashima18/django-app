# Generated by Django 2.2.2 on 2019-06-26 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0015_auto_20190626_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img5', models.ImageField(upload_to='images/')),
                ('p', models.TextField(help_text='Enter a brief description', max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='footer',
            name='img5',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='p',
        ),
    ]
