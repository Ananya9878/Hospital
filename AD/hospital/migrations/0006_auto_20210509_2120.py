# Generated by Django 3.1.7 on 2021-05-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_departmentimage_hospitalimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='hospital',
            name='pincode',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='hospital',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]