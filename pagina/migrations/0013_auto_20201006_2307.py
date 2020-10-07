# Generated by Django 3.0.4 on 2020-10-07 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0012_auto_20201005_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioincripcion',
            name='telefono',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='formularioincripcion',
            name='telefono_local',
            field=models.IntegerField(verbose_name='Telefono Local'),
        ),
        migrations.CreateModel(
            name='FormularioTecnicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=8)),
                ('archivo_cedula', models.ImageField(blank=True, null=True, upload_to='')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=70)),
                ('direccion', models.TextField(verbose_name='Dirección')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('telefono_local', models.IntegerField(verbose_name='Telefono Local')),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('curriculum', models.ImageField(blank=True, null=True, upload_to='')),
                ('institucion_educativa', models.CharField(max_length=50)),
                ('trabajo', models.BooleanField(default=True)),
                ('tipo_ente', models.CharField(blank=True, max_length=50, null=True)),
                ('ente_trabajador', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=True, verbose_name='Estatus Registrado')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.Estados')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.Municipios')),
                ('nivel_academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.NivelAcademico')),
            ],
            options={
                'verbose_name': 'Formulario Para Tecnicos',
                'verbose_name_plural': 'Formulario Para Tecnicos',
                'db_table': 'formulario_tecnicos',
                'ordering': ['id'],
            },
        ),
    ]
