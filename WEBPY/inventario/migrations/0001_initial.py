# Generated by Django 5.0.4 on 2024-04-30 08:35

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleTransferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Situacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadOrganica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordenCompra', models.IntegerField()),
                ('proveedor', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=20)),
                ('fechaVenGarantia', models.CharField(max_length=20)),
                ('componentes', models.CharField(max_length=50)),
                ('descripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.descripcion')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.estado')),
                ('situacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.situacion')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleSalida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antecedentes', models.CharField(max_length=200)),
                ('analisis', models.CharField(max_length=1000)),
                ('conclusiones', models.CharField(max_length=300)),
                ('recomendaciones', models.CharField(max_length=200)),
                ('asunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.asunto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('dni', models.CharField(max_length=10)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.estado')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.rol')),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.sede')),
                ('unidadOrganica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.unidadorganica')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.CharField(max_length=20)),
                ('fechaEliminacion', models.CharField(max_length=20)),
                ('movimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.movimiento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('situacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.situacion')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleProceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UsuarioInicial', models.CharField(max_length=20)),
                ('unidadOrganicaInicial', models.CharField(max_length=20)),
                ('sedeInicial', models.CharField(max_length=20)),
                ('UsuarioFinal', models.CharField(max_length=20)),
                ('unidadOrganicaFinal', models.CharField(max_length=20)),
                ('sedeFinal', models.CharField(max_length=20)),
                ('bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.bien')),
                ('detalleSalida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.detallesalida')),
                ('detalleTransferencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.detalletransferencia')),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.proceso')),
            ],
        ),
    ]
