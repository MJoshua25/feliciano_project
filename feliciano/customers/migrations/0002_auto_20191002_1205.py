# Generated by Django 2.2.5 on 2019-10-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterchef',
            name='user',
        ),
        migrations.AddField(
            model_name='masterchef',
            name='fontion',
            field=models.CharField(default='ok ', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='masterchef',
            name='nom',
            field=models.CharField(default='pentest', max_length=255),
            preserve_default=False,
        ),
    ]