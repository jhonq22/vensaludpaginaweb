# Generated by Django 3.0.4 on 2020-10-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0011_auto_20201004_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioincripcion',
            name='archivo_cedula',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='formularioincripcion',
            name='curriculum',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
