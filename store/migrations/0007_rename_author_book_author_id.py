# Generated by Django 3.2.3 on 2022-06-11 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_booksmodel_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author_id',
        ),
    ]
