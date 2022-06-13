# Generated by Django 3.2.3 on 2022-06-13 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20220613_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='status',
            field=models.CharField(choices=[('out of stock', 'out of stock'), ('critical', 'critical'), ('good', 'good'), ('bad', 'bad')], max_length=255),
        ),
    ]
