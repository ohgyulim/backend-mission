# Generated by Django 4.0.1 on 2022-01-14 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_delete_item_delete_qa_delete_review_delete_store'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]