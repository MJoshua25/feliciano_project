# Generated by Django 2.2.5 on 2019-10-02 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0002_menu_image_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.IntegerField()),
                ('titre', models.CharField(max_length=225)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=225)),
                ('titre', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('image1', models.ImageField(blank=True, upload_to='img')),
                ('image2', models.ImageField(blank=True, upload_to='img')),
                ('jour_debut', models.DateTimeField()),
                ('jour_fin', models.DateTimeField()),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('contact', models.TimeField()),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=225)),
                ('titre', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
