# Generated by Django 3.0.7 on 2020-06-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
