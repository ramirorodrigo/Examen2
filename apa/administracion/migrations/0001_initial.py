# Generated by Django 3.2.8 on 2021-10-29 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(help_text='Introdusca el número CI', max_length=10, unique=True)),
                ('nombres', models.CharField(help_text='Intrusca nombres', max_length=20)),
                ('apellidos', models.CharField(help_text='Intrusca apellidos', max_length=20)),
                ('direccion', models.CharField(blank=True, help_text='Intrusca direccion', max_length=20, null=True)),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'ordering': ['-apellidos', 'nombres'],
            },
        ),
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_lector', models.CharField(max_length=7, unique=True)),
                ('usuario_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Bibliotecario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_bibli', models.CharField(max_length=7, unique=True)),
                ('usuario_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario')),
            ],
        ),
    ]
