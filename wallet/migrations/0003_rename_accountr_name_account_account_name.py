# Generated by Django 4.0.6 on 2022-09-02 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_account_wallet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='accountr_name',
            new_name='account_name',
        ),
    ]
