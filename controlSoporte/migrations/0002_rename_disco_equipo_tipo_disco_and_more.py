# Generated by Django 5.0.1 on 2024-02-03 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlSoporte', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='disco',
            new_name='tipo_disco',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='tipo',
            new_name='tipo_equipo',
        ),
    ]
