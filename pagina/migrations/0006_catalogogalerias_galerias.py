# Generated by Django 3.0.4 on 2020-10-03 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_auto_20201001_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galerias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_galeria', models.CharField(max_length=80, verbose_name='Nombre Galería')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('imagen_principal', models.ImageField(blank=True, null=True, upload_to='')),
                ('status', models.BooleanField(default=True, verbose_name='Estatus Publicación')),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galerias',
                'db_table': 'galerias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CatalogoGalerias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_principal', models.ImageField(blank=True, null=True, upload_to='')),
                ('galeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.Galerias')),
            ],
            options={
                'verbose_name': 'Catologo de Galeria',
                'verbose_name_plural': 'Catalogo de Galerias',
                'db_table': 'catalogo_galerias',
                'ordering': ['id'],
            },
        ),
    ]
