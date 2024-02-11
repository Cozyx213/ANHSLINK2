# Generated by Django 5.0.1 on 2024-02-08 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='haha@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='grade',
            field=models.IntegerField(),
        ),
    ]