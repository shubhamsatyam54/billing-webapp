# Generated by Django 3.2.4 on 2022-01-24 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_auto_20220124_0618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='country',
            new_name='batch',
        ),
    ]
