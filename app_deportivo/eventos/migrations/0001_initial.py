# Generated by Django 3.2.13 on 2024-07-02 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('federaciones', '0001_initial'),
        ('instalaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('federacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='federaciones.federacion')),
                ('instalacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instalaciones.instalacion')),
            ],
        ),
    ]
