# Generated by Django 3.2.3 on 2022-06-11 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('YearOfPublication', models.DateField(default=None)),
                ('description', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='store.author')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]