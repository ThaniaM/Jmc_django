# Generated by Django 5.0.1 on 2024-02-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlCliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
