# Generated by Django 4.1.2 on 2023-04-07 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_user_account_alter_flavor_acctusername'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='User',
        ),
    ]
