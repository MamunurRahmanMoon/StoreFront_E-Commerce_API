# Generated by Django 4.2.7 on 2023-11-18 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view history', 'Can view history')]},
        ),
    ]
