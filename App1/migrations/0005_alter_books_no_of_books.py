# Generated by Django 4.0.5 on 2022-06-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0004_alter_books_no_of_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='No_of_books',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]