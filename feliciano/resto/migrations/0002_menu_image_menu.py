# Generated by Django 2.2.5 on 2019-10-01 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image_menu',
            field=models.ImageField(default='image.png', upload_to='Menu'),
            preserve_default=False,
        ),
    ]
