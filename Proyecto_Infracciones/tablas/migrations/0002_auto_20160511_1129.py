# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 16:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudad',
            old_name='ID_Departamento',
            new_name='Departamento',
        ),
        migrations.RenameField(
            model_name='infracciones',
            old_name='ID_Persona',
            new_name='Persona',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='ID_Casa',
            new_name='Casa',
        ),
        migrations.RenameField(
            model_name='modelo',
            old_name='ID_Marca',
            new_name='Marca',
        ),
        migrations.RenameField(
            model_name='multa',
            old_name='ID_Infracciones',
            new_name='Infracciones',
        ),
        migrations.RenameField(
            model_name='multa',
            old_name='ID_Persona',
            new_name='Persona',
        ),
        migrations.RenameField(
            model_name='multa',
            old_name='ID_vehicuo',
            new_name='vehicuo',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='ID_Ciudad',
            new_name='Ciudad',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='ID_Tipo_Persona',
            new_name='Tipo_Persona',
        ),
        migrations.RenameField(
            model_name='vehiculo',
            old_name='ID_Modelo',
            new_name='Modelo',
        ),
        migrations.RenameField(
            model_name='vehiculo',
            old_name='ID_Persona',
            new_name='Persona',
        ),
    ]