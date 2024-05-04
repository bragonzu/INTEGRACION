from django.db import models
from django.contrib.auth.models import AbstractUser
from inventario.managers import UserManager

class Sede(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre}'

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre}'

class UnidadOrganica(models.Model):
    nombre = models.CharField(max_length=50)    
    def __str__(self):
        return f'{self.nombre}'

class Estado(models.Model):
    nombre = models.CharField(max_length=50)   
    def __str__(self):
        return f'{self.nombre}'

class Usuario(AbstractUser):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255,)
    dni = models.CharField(max_length=10)
    unidadOrganica = models.ForeignKey(UnidadOrganica, on_delete=models.CASCADE, null=True, blank=True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, blank=True)

    # Campos configurables adicionales
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    

class Movimiento(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre}'

class Proceso(models.Model):
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE)
    fechaIngreso = models.CharField(max_length=20)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaEliminacion = models.CharField(max_length=20)

class TipoBien(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre}'

class Bien(models.Model):
    tipoBien = models.ForeignKey(TipoBien, on_delete=models.CASCADE)
    ordenCompra = models.IntegerField()
    proveedor = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=20)
    fechaVenGarantia = models.CharField(max_length=20)
    componentes = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class DetalleTransferencia(models.Model):
    motivo = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)

class Asunto(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nombre}'

class DetalleSalida(models.Model):
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE)
    antecedentes = models.CharField(max_length=200)
    analisis = models.CharField(max_length=1000)
    conclusiones = models.CharField(max_length=300)
    recomendaciones = models.CharField(max_length=200)

class DetalleProceso(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    UsuarioInicial = models.CharField(max_length=20)
    unidadOrganicaInicial = models.CharField(max_length=20)
    sedeInicial = models.CharField(max_length=20)
    UsuarioFinal = models.CharField(max_length=20)
    unidadOrganicaFinal = models.CharField(max_length=20)
    sedeFinal = models.CharField(max_length=20)
    # funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    detalleTransferencia = models.ForeignKey(DetalleTransferencia, on_delete=models.CASCADE)
    detalleSalida = models.ForeignKey(DetalleSalida, on_delete=models.CASCADE)

