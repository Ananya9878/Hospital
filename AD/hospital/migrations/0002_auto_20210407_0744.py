# Generated by Django 3.1.7 on 2021-04-07 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='discription',
            new_name='description',
        ),
    ]