from django.db import models

# Create your models here.
class Caratenvue(models.Model):
    cargo = models.CharField(primary_key=True,max_length=3)
    nombre = models.CharField(null=True,max_length=40)
    creado_por = models.CharField(null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(null=True,max_length=1)
    modificado_por = models.CharField(null=True,max_length=10)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
        managed = False
        db_table = 'caratenvue'

class Caratvue(models.Model):
    fecha = models.DateField(primary_key=True)
    compania = models.CharField(max_length=3)
    matricula = models.CharField(max_length=15)
    aeronave = models.CharField(max_length=2)
    fecha_llegada = models.DateField()
    hora_llegada = models.TimeField()
    creado_por = models.CharField(max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    monto_servicio = models.DecimalField(max_digits=14, decimal_places=2,null=True)
    cia_afec = models.CharField(max_length=3,null=True)
    agen_afec = models.CharField(max_length=3,null=True)
    codigo = models.CharField(max_length=3,null=True)
    factura = models.CharField(max_length=7,null=True)
    no_afectacion = models.IntegerField(null=True)
    status = models.CharField(max_length=1)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
        managed = False
        db_table ='caratvue'
        unique_together = ('fecha', 'compania', 'matricula')

class Carcmani(models.Model):
    fecha = models.DateField(null=False,primary_key=True)
    operador = models.CharField(max_length=3, null=False)
    numero_vuelo = models.CharField(max_length=20, null=False)
    puerto_despacho = models.CharField(max_length=6, null=False)
    puerto_destino = models.CharField(max_length=6, null=False) 
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField(null=False)
    hora_creado = models.TimeField(null=False)
    status = models.CharField(max_length=1,null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
        managed = False
        db_table = 'carcmani'
        unique_together = ('fecha', 'operador', 'numero_vuelo')

class Carcoaer(models.Model):
    compania = models.CharField(max_length=3, null=False,primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField(null=False)
    hora_creado = models.TimeField(null=False)
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10, null=True) 
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
         managed = False
         db_table = 'carcoaer'

class Cardeent(models.Model):
    fecha = models.DateField(null=False,primary_key=True)
    fecha_manifiesto = models.DateField(null=False) 
    operador = models.CharField(max_length=3, null=False)
    numero_vuelo = models.CharField(max_length=20, null=False)
    no_embarque = models.CharField(max_length=20, null=False)
    tarifa = models.CharField(max_length=2, null=False)
    monto = models.DecimalField(max_digits=14, decimal_places=2, null=True) 
    status = models.CharField(max_length=1, null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
       managed = False
       db_table = 'cardeent'
       unique_together = ('fecha', 'fecha_manifiesto', 'operador','numero_vuelo','no_embarque','tarifa')

class Cardmani(models.Model):
    fecha = models.DateField()
    operador = models.CharField(null=True,max_length=3)
    numero_vuelo = models.CharField(null=True,max_length=20)
    no_embarque = models.CharField(null=True,max_length=20)
    secuencia = models.SmallIntegerField()
    naturaleza = models.CharField(null=True,max_length=3)
    bar_code = models.CharField(null=True,max_length=20)
    cant_items = models.IntegerField()
    remitente = models.CharField(max_length=250)
    destinatario = models.CharField(max_length=250)
    comentarios = models.CharField(null=True,max_length=250)
    peso_kg = models.DecimalField(max_digits=14, decimal_places=2,  null=True)
    peso_lb = models.DecimalField(max_digits=14, decimal_places=2,  null=True)
    no_udl = models.CharField(null=True,max_length=20)
    almacen = models.CharField(null=True,max_length=2)
    area = models.CharField(null=True,max_length=2)
    anaquel = models.CharField(null=True,max_length=3)
    cara = models.CharField(null=True,max_length=1)
    nivel = models.CharField(null=True,max_length=2)
    posicion = models.CharField(null=True,max_length=1)
    status = models.CharField(null=True,max_length=1)
    modificado_por = models.CharField(null=True,max_length=10)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
        managed = False
        db_table = 'cardmani'
        unique_together = (('fecha', 'operador', 'numero_vuelo', 'no_embarque', 'secuencia'),)


class Carentre(models.Model):
    fecha = models.DateField()
    fecha_manifiesto = models.DateField()
    operador = models.CharField( null=True,max_length=3)
    numero_vuelo = models.CharField(null=True,max_length=20)
    no_embarque = models.CharField(null=True,max_length=20)
    secuencia = models.SmallIntegerField()
    entregado_a = models.CharField(null=True,max_length=50)
    cedula = models.CharField(null=True,max_length=15)
    no_placa = models.CharField(null=True,max_length=15)
    docto_aduana = models.CharField(null=True,max_length=20)
    recibo_pag = models.CharField(null=True,max_length=20)
    piezas_entrega = models.IntegerField()
    piezas_faltantes = models.IntegerField()
    piezas_buenas = models.IntegerField()
    observacion = models.CharField(null=True,max_length=250)
    cia_afec = models.CharField(null=True,max_length=3)
    agen_afec = models.CharField(null=True,max_length=3)
    codigo = models.CharField(null=True,max_length=3)
    factura = models.CharField(null=True,max_length=7)
    monto = models.DecimalField(max_digits=14, decimal_places=2,  null=True)
    no_afectacion = models.IntegerField( null=True)
    status = models.CharField(null=True,max_length=1)
    no_liqudacion = models.CharField(null=True,max_length=20)

    class Meta:
        managed = False
        db_table = 'carentre'
        unique_together = (('fecha', 'fecha_manifiesto', 'operador', 'numero_vuelo', 'no_embarque', 'secuencia'),)


class Cargcaman(models.Model):
    cargo = models.CharField(primary_key=True,max_length=2)
    nombre = models.CharField(null=True,max_length=50)
    creado_por = models.CharField(null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(null=True,max_length=1)
    modificado_por = models.CharField(null=True,max_length=10)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
        managed = False
        db_table = 'cargcaman'
    

class Carinent(models.Model):
    tipo = models.CharField(null=True,max_length=1)
    codigo = models.CharField(null=True,max_length=2)
    descripcion = models.CharField(null=True,max_length=40)
    creado_por = models.CharField(null=True,max_length=1)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(null=True,max_length=1)
    modificado_por = models.CharField(null=True,max_length=10)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
        managed = False
        db_table = 'carinent'
        unique_together = (('tipo', 'codigo'),)


class Carnatur(models.Model):
    naturaleza = models.CharField(primary_key=True,max_length=3)
    nombre = models.CharField(null=True,max_length=50)
    cargo = models.CharField(null=True, max_length=3)
    creado_por = models.CharField(null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(null=True,max_length=1)
    modificado_por = models.CharField(null=True, max_length=10)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
        managed = False
        db_table = 'carnatur'


class Caropera(models.Model):
    operador = models.CharField(primary_key=True,max_length=3)
    nombre = models.CharField(null=True,max_length=40)
    creado_por = models.CharField(null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(null=True,max_length=1)
    modificado_por = models.CharField(null=True,max_length=10)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
        managed = False
        db_table = 'caropera'

class Cartaralm(models.Model):
    id = models.AutoField( primary_key=True, null=False)
    tarifa = models.CharField( null=True,max_length=2)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField(null=True)
    creado_por = models.CharField(null=True,max_length=10)
    fecha_creado = models.DateField(null=True)
    hora_creado = models.TimeField(null=True)
    peso_base = models.DecimalField(max_digits=5, decimal_places=2,  null=True)
    medida = models.CharField(null=True,max_length=7)
    valor_base = models.DecimalField(max_digits=12, decimal_places=2,  null=True)
    peso_adicional = models.DecimalField(max_digits=8, decimal_places=2,  null=True)
    valor_peso_adic = models.DecimalField(max_digits=12, decimal_places=2,  null=True)
    status = models.CharField( null=True,max_length=1)
    modificado_por = models.CharField( null=True,max_length=10)
    fecha_status = models.DateField( null=True)
    hora_status = models.TimeField( null=True)

    class Meta:
        managed = False
        db_table = 'cartaralm'
        unique_together = (('tarifa', 'fecha_inicio'),)


class Cartari(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    tarifa = models.CharField( null=True,max_length=2)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField( null=True)
    creado_por = models.CharField( null=True,max_length=10)
    fecha_creado = models.DateField( null=True)
    hora_creado = models.TimeField( null=True)
    entrada = models.DecimalField(max_digits=14, decimal_places=2,  null=True)
    costo_diario = models.DecimalField(max_digits=14, decimal_places=2,  null=True)
    medida = models.CharField( null=True,max_length=7)
    minimo_diario = models.DecimalField(max_digits=14, decimal_places=2,  null=True)
    full_pallet = models.DecimalField(max_digits=14, decimal_places=2,  null=True)
    status = models.CharField( null=True,max_length=1)
    modificado_por = models.CharField( null=True,max_length=10)
    fecha_status = models.DateField( null=True)
    hora_status = models.TimeField( null=True)

    class Meta:
        managed = False
        db_table = 'cartari'
        unique_together = (('tarifa', 'fecha_inicio'),)


class Cartarman(models.Model):
    id = models.AutoField( primary_key=True, null=False)
    tarifa = models.CharField( null=True,max_length=2)
    fecha_inicio = models.DateField()
    cargo = models.CharField( null=True,max_length=2)
    fecha_final = models.DateField()
    creado_por = models.CharField( null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField( null=True,max_length=1)
    valor = models.DecimalField(max_digits=12, decimal_places=5)
    aplica = models.CharField( null=True,max_length=1)
    modificado_por = models.CharField(null=True,max_length=10)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
        managed = False
        db_table = 'cartarman'
        unique_together = (('tarifa', 'cargo', 'fecha_inicio'),)


class Cartarvue(models.Model):
    id = models.AutoField( primary_key=True, default=0, null=False )
    aeronave = models.CharField( null=True,max_length=2)
    fecha_inicio = models.DateField()
    cargo = models.CharField( null=True,max_length=3)
    fecha_final = models.DateField()
    creado_por = models.CharField( null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    costo_hora = models.DecimalField(max_digits=14, decimal_places=2)
    status = models.CharField( null=True,max_length=1)
    modificado_por = models.CharField( null=True,max_length=10)
    fecha_status = models.DateField( null=True)
    hora_status = models.TimeField( null=True)

    class Meta:
        managed = False
        db_table = 'cartarvue'
        unique_together = (('aeronave', 'fecha_inicio', 'cargo'),)


class Cartiaero(models.Model):
    aeronave = models.CharField(primary_key=True,max_length=2)
    descripcion = models.CharField( null=True,max_length=20)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    creado_por = models.CharField( null=True,max_length=10)
    status = models.CharField( null=True,max_length=1)
    modificado_por = models.CharField( null=True,max_length=10)
    fecha_status = models.DateField( null=True)
    hora_status = models.TimeField( null=True)

    class Meta:
        managed = False
        db_table = 'cartiaero'

class Cartitar(models.Model):
    tarifa = models.CharField(primary_key=True,max_length=2)
    nombre = models.CharField( null=True,max_length=40)
    creado_por = models.CharField( null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    tipo = models.CharField( null=True,max_length=1)
    status = models.CharField( null=True,max_length=1)
    modificado_por = models.CharField( null=True,max_length=10)
    fecha_status = models.DateField( null=True)
    hora_status = models.TimeField( null=True)

    class Meta:
        managed = False
        db_table = 'cartitar'


class Carudls(models.Model):
    no_udl = models.CharField(primary_key=True,max_length=20)
    cant_items = models.IntegerField()
    almacen = models.CharField( null=True,max_length=2)
    area = models.CharField( null=True,max_length=2)
    anaquel = models.CharField( null=True,max_length=3)
    cara = models.CharField( null=True,max_length=1)
    nivel = models.CharField( null=True,max_length=2)
    posicion = models.CharField( null=True,max_length=1)
    status = models.CharField( null=True,max_length=1)
    modificado_por = models.CharField( null=True,max_length=10)
    fecha_status = models.DateField( null=True)
    hosta_status = models.TimeField( null=True)

    class Meta:
        managed = False
        db_table = 'carudls'

class Ciudades(models.Model):
    pais = models.CharField( null=True,max_length=3)
    ciudad = models.CharField( primary_key=True,max_length=5)
    nombre = models.CharField( null=True,max_length=50)
    status = models.CharField(null= False, max_length=1)

    class Meta:
        managed = False
        db_table = 'ciudades'
        unique_together = (('pais', 'ciudad'),)

class Clientes(models.Model):
    empresa = models.CharField(primary_key=True,max_length=7)
    nombre = models.CharField( null=True,max_length=50)
    creado_por = models.CharField( null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    direccion = models.CharField(max_length=250)
    telefono = models.CharField( null=True,max_length=15)
    telefono2 = models.CharField( null=True,max_length=15)
    correo = models.CharField( null=True,max_length=80)
    corrreo2 = models.CharField( null=True,max_length=80)
    contacto = models.CharField( null=True,max_length=50)
    ubicacion = models.CharField( null=True,max_length=10)
    status = models.CharField( null=True,max_length=1)
    modificado_por = models.CharField( null=True,max_length=10)
    fecha_status = models.DateField( null=True)
    hora_status = models.TimeField( null=True)

    class Meta:
        managed = False
        db_table = 'clientes'

class Crmcorr(models.Model):
    pais = models.CharField( null=True,max_length=3)
    provincia = models.CharField( null=True,max_length=2)
    ciudad = models.CharField( null=True,max_length=2)
    distrito = models.CharField( null=True,max_length=2)
    corregimiento = models.CharField( null=True,max_length=2)
    nombre = models.CharField( null=True,max_length=40)
    tel_central = models.CharField( null=True,max_length=4)
    creado_por = models.CharField( null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField( null=True)
    modificado_por = models.CharField( null=True,max_length=10)
    status = models.CharField( null=True,max_length=1)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'crmcorr'
        unique_together = (('pais', 'provincia', 'ciudad', 'distrito', 'corregimiento'),)


class Crmprov(models.Model):
    pais = models.CharField( null=True,max_length=3)
    provincia = models.CharField( null=True,max_length=2)
    nombre = models.CharField( null=True,max_length=40)
    creado_por = models.CharField( null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    modificado_por = models.CharField( null=True,max_length=10)
    status = models.CharField( null=True,max_length=1)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'crmprov'
        unique_together = (('pais', 'provincia'),)


class Caratvued(models.Model):
    fecha = models.DateField(primary_key=True)
    compania = models.CharField(max_length=3, null=False)
    matricula = models.CharField(max_length=15, null=False)
    cargo = models.CharField(max_length=3, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField(null=False)
    hora_creado = models.TimeField(null=False)
    fecha_inicio = models.DateField(null=True)
    hora_inicio = models.TimeField(null=True)
    fecha_final = models.DateField(null=True)
    hora_final = models.TimeField(null=True)
    tiempo_total = models.TimeField(null=True)
    monto = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10, null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.TimeField(null=True)

    class Meta:
        managed = False
        db_table = 'caratvued'
        unique_together = ('fecha', 'compania', 'matricula', 'cargo')


class Logubica(models.Model):
    ubicacion = models.AutoField(primary_key= True)
    almacen = models.CharField( null=True,max_length=2)
    area = models.CharField( null=True,max_length=2)
    anaquel = models.CharField( null=True,max_length=3)
    cara = models.CharField( null=True,max_length=1)
    fila = models.CharField( null=True,max_length=2)
    columna = models.CharField( null=True,max_length=1)
    creado_por = models.CharField( null=True,max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField( null=True,max_length=1)
    modificado_por = models.CharField( null=True,max_length=10)
    fecha_status = models.DateField( null=True)
    hora_status = models.TimeField( null=True)

    class Meta:
        managed = False
        db_table = 'logubica'
        unique_together = ('almacen', 'area', 'anaquel', 'cara', 'fila', 'columna')
         

class Logarea(models.Model):
    id = models.AutoField( primary_key=True, default=0, null=False )
    almacen = models.CharField( null=False, max_length=2)
    area = models.CharField(null= False, max_length=2)
    descripcion = models.CharField(null= False, max_length=30)
    creado_por = models.CharField(null= False, max_length=10)
    fecha_creado = models.DateField(null= False)
    hora_creado = models.TimeField(null= False)
    modificado_por = models.CharField(null= True, max_length=10)
    fecha_status = models.DateField(null= True)
    hora_status = models.TimeField(null= True)

    class Meta:
        managed = False
        db_table = 'logarea'
        unique_together = ('almacen', 'area')
        
class Logalma(models.Model):
    almacen = models.CharField(primary_key= True, max_length=2)
    descripcion = models.CharField(null= False, max_length=40)
    creado_por = models.CharField(null= False, max_length=10)
    fecha_creado = models.DateField(null= False)
    hora_creado = models.TimeField(null= False)
    fecha_trabajo = models.DateField(null= False)
    max_dias_cierre = models.SmallIntegerField()
    compania = models.CharField(max_length=3)
    gerencia = models.CharField(max_length=2)
    agencia = models.CharField(max_length=3)
    principal = models.CharField(max_length=1)
    factura = models.CharField(max_length=1)
    tipo_almacen = models.CharField(max_length=1)
    reserva = models.CharField(max_length=1)
    dias_reserva = models.SmallIntegerField()
    maneja_despacho = models.CharField(max_length=1)
    dias_despachar = models.SmallIntegerField()
    secuencia_reserva = models.SmallIntegerField()
    totales_ctrl = models.CharField(max_length=1)
    tipo_costo = models.CharField(max_length=1)
    modificado_por = models.CharField(max_length=10)
    status = models.CharField(max_length=1)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    genera_asiento = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'logalma'
        
class Loganaquel(models.Model):
    id = models.AutoField( primary_key=True, default=0, null=False )
    almacen = models.CharField(null= False, max_length=2)
    area = models.CharField(null= False, max_length=2)
    anaquel = models.CharField(null= False, max_length=2)
    cara = models.CharField(null= False, max_length=1)
    creado_por = models.CharField(null= False, max_length=10)
    fecha_creado = models.DateField(null= False)
    hora_creado = models.TimeField(null= False)
    modificado_por = models.CharField(max_length=10)
    status = models.CharField(null=False, max_length=1)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'loganaquel'
        unique_together = (('almacen', 'area', 'anaquel', 'cara'),)

class Paises(models.Model):
    pais = models.CharField(primary_key=True,max_length=3)
    nombre = models.CharField( null=True,max_length=50)
    name = models.CharField( null=True,max_length=50)
    iso2 = models.CharField( null=True,max_length=3)
    iso3 = models.CharField( null=True,max_length=4)
    phone_code = models.CharField( null=True,max_length=7)
    status = models.CharField(null= False, max_length=1)

    class Meta:
        managed = False
        db_table = 'paises'

class Puertos(models.Model):
    puerto = models.CharField(max_length=8,primary_key=True)
    nombre = models.CharField( null=True,max_length=40)
    pais = models.CharField( null=True,max_length=3)
    ciudad = models.CharField( null=True,max_length=5)
    tipo = models.CharField( null=True,max_length=1)
    status = models.CharField(null= False, max_length=1)

    class Meta:
        managed = False
        db_table = 'puertos'

class Ubicacion(models.Model):
    codigo = models.CharField(primary_key=True,max_length=10)
    provincia = models.CharField( null=True,max_length=2)
    nprovincia = models.CharField( null=True,max_length=50)
    distrito = models.CharField( null=True,max_length=2)
    ndistrito = models.CharField( null=True,max_length=50)
    corregimiento = models.CharField( null=True,max_length=2)
    ncorregimiento = models.CharField( null=True,max_length=100)

    class Meta:
        managed = False
        db_table = 'ubicacion'