from django.db import models

class Proveedor(models.Model):
    ruc = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return self.razon_social

class Categoria(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.codigo}: {self.nombre}'

class DetallePedido(models.Model):

    pedido = models.ForeignKey('Pedido', on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)

    cantidad = models.FloatField()
    subtotal = models.FloatField()

    def __str__(self):
        return f'{self.subtotal}'

class Usuario (models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    documentoIdentidad = models.CharField(max_length=8)
    nombres = models.CharField(max_length=20)
    apellidoPaterno = models.CharField(max_length=20)
    apellidoMaterno = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
    fechaNacimiento = models.DateField
    fechaCreacion = models.DateField
    estado = models.TextField()

    def __str__(self):
        return f'{self.documentoIdentidad}'

class Cliente(models.Model):

    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    preferencias = list()

    def __str__(self):
        return f'{self.preferencias}'

class Colaborador(models.Model):

    reputacion = models.FloatField()
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    coberturaEntrega = models.ForeignKey('Localizacion', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.reputacion}'

class Localizacion(models.Model):
  distrito = models.CharField(max_length=20)
  provincia = models.CharField(max_length=20)
  departamento = models.CharField(max_length=20)

  def __str__(self):
        return f'{self.distrito}, {self.provincia}, {self.departamento}'

class Pedido(models.Model):
  fechaCreacion = models.DateField
  estado = models.CharField(max_length=10)
  fechaEntrega = models.DateField
  direccionEntrega = models.TextField()
  cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
  repartidor = models.ForeignKey('Colaborador', on_delete=models.SET_NULL, null=True)
  ubicacion = models.ForeignKey('Localizacion', on_delete=models.SET_NULL, null=True)
  tarifa = models.FloatField()

  def __str__(self):
        return f'{self.tarifa}'

class Producto(models.Model):
    # Relaciones
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)

    # Atributos
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.FloatField()
    estado = models.CharField(max_length=3)
    descuento = models.FloatField(default=0)

    def __str__(self):
        return self.nombre

    def precio_final(self):
        return self.precio * (1 - self.descuento)

    def sku(self):
        codigo_categoria = self.categoria.codigo.zfill(4)
        codigo_producto = str(self.id).zfill(6)

        return f'{codigo_categoria}-{codigo_producto}'
