# Generated by Django 2.0.8 on 2018-09-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default='img/default.jpg', upload_to='profile_picture'),
        ),
    ]