# Generated by Django 5.0.2 on 2024-04-26 02:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='subdepartamento',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='sub_departamento',
        ),
        migrations.AlterModelOptions(
            name='documento',
            options={'permissions': [('eliminar_documento', 'Eliminar documento')]},
        ),
        migrations.AddField(
            model_name='documento',
            name='año',
            field=models.CharField(default='2024', max_length=5),
        ),
        migrations.AddField(
            model_name='documento',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documento',
            name='departamento',
            field=models.CharField(choices=[('Contabilidad', 'Contabilidad'), ('RRHH', 'RRHH'), ('Informatica', 'Informatica')], default='Informatica', max_length=20),
        ),
        migrations.AddField(
            model_name='documento',
            name='documento',
            field=models.CharField(choices=[('General', 'General'), ('Circular', 'Circular'), ('Minuta', 'Minuta'), ('Nota', 'Nota'), ('Oficio', 'Oficio')], default='General', max_length=20),
        ),
        migrations.AddField(
            model_name='documento',
            name='mes',
            field=models.CharField(default='01', max_length=5),
        ),
        migrations.AddField(
            model_name='documento',
            name='modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='folio',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='documento',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.DeleteModel(
            name='SubDepartamento',
        ),
    ]
