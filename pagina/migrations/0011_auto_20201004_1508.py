# Generated by Django 3.0.4 on 2020-10-04 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0010_auto_20201004_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioincripcion',
            name='archivo_cedula',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Adjuntar Cedula'),
        ),
    ]