# Generated by Django 5.0.3 on 2024-04-15 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_grade_section_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='section',
        ),
    ]