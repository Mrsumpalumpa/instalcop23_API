# Generated by Django 4.2.16 on 2024-12-01 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='codigo_obra',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='cliente',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='detalles_adicionales',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='nombre_proyecto',
            new_name='project_name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='fecha_inicio',
            new_name='start_date',
        ),
    ]
