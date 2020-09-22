# Generated by Django 3.1 on 2020-09-22 19:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book_review',
            new_name='Book_reviews',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='release_date',
            new_name='pub_date',
        ),
    ]
