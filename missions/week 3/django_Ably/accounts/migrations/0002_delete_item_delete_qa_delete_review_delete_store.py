# Generated by Django 4.0.1 on 2022-01-14 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='QA',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
