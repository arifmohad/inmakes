# Generated by Django 3.2.20 on 2023-08-02 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default=22, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
