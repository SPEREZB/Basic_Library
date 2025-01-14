# Generated by Django 3.2.8 on 2022-04-29 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='Titulo')),
                ('imagenes', models.ImageField(null=True, upload_to='Images', verbose_name='Imagen')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
