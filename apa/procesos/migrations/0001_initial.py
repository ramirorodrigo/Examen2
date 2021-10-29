# Generated by Django 3.2.8 on 2021-10-29 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Adquisicion', '0001_initial'),
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procesos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(blank=True, help_text='Intrusca el detalle', max_length=77, null=True)),
                ('fecha', models.DateTimeField()),
                ('biblio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administracion.bibliotecario')),
                ('lect', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administracion.lector')),
                ('libro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Adquisicion.libros')),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_prestamo', models.CharField(max_length=7, unique=True)),
                ('fecha_pres', models.DateTimeField()),
                ('proceso_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='procesos.procesos')),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_devolucion', models.CharField(max_length=7, unique=True)),
                ('fecha_dev', models.DateTimeField()),
                ('proceso_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='procesos.procesos')),
            ],
        ),
    ]