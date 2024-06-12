# Generated by Django 3.2.13 on 2024-06-12 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('edad_minima', models.IntegerField()),
                ('edad_maxima', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.deporte')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Federacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('contacto', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('rol', models.CharField(choices=[('atleta', 'Atleta'), ('entrenador', 'Entrenador'), ('administrador', 'Administrador')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.IntegerField()),
                ('tiempo', models.TimeField()),
                ('puntos', models.IntegerField()),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.atleta')),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.competencia')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipacionAtleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.CharField(blank=True, max_length=100, null=True)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.atleta')),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.competencia')),
            ],
        ),
        migrations.CreateModel(
            name='Medalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.atleta')),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.competencia')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.atleta')),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.competencia')),
            ],
        ),
        migrations.CreateModel(
            name='EventoSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.evento')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.sponsor')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='federacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.federacion'),
        ),
        migrations.AddField(
            model_name='evento',
            name='instalacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.instalacion'),
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.deporte')),
                ('entrenador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.entrenador')),
                ('federacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.federacion')),
            ],
        ),
        migrations.CreateModel(
            name='Entrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.atleta')),
                ('entrenador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.entrenador')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.deporte')),
            ],
        ),
        migrations.AddField(
            model_name='competencia',
            name='deporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.deporte'),
        ),
        migrations.AddField(
            model_name='competencia',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.disciplina'),
        ),
        migrations.AddField(
            model_name='competencia',
            name='instalacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.instalacion'),
        ),
        migrations.AddField(
            model_name='atleta',
            name='deporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.deporte'),
        ),
        migrations.AddField(
            model_name='atleta',
            name='entrenador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.entrenador'),
        ),
        migrations.AddField(
            model_name='atleta',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.equipo'),
        ),
        migrations.AddField(
            model_name='atleta',
            name='federacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_deportivo.federacion'),
        ),
    ]