
 export interface Natur{
    naturaleza?:string,
    nombre?:string,
    cargo?:string,
    creado_por?:string,
    fecha_creado?:string,
    hora_creado?:string,
    status?:string,
    modificado_por?:string,
    fecha_status?:string,
    hora_status?:string
    nom_cargo?:string
    nom_status?:string
}

export interface Paises{
    pais?:string
    nombre?:string
    name?:string
    iso2?:string
    iso3?:string
    phone_code?:string
}

export interface Ciudades{
    pais?:string
    ciudad?:string
    nombre?:string
    nombre_pais?:string
}

export interface Puertos{
    puerto?:string
    nombre?:string
    pais?:string
    ciudad?:string
    tipo?:string
    nombre_pais?:string
    nombre_ciudad?:string
}

export interface Cartarvue{
    aeronave?:string
    fecha_inicio?:string
    fecha_final?:string
    cargo?:string
    costo_hora?:string
    status?:string
    nombre_cargo?:string
    nom_status?:string
}

export interface Cartiaero{
    aeronave?:string
    descripcion?:string
    status?:string
    nom_status?:string
}

export interface Caratenvue{
    cargo?:string
    nombre?:string
    status?:string
    nom_status?:string
}

export interface Cartarman{
    tarifa?:string
    cargo?:string
    fecha_inicio?:string
    fecha_final?:string
    valor?:string
    aplica?:string
    nom_aplica?:string
    status?:string
    nom_status?:string

}

export interface Cartitar
{
    tarifa?:string
    nombre?:string
    status?:string
}

export interface Cargcaman
{
    cargo?:string
    nombre?:string
    creado_por?:string
    fecha_creado?:string
    hora_creado?:string
    status?:string
    modificado_por?:string
    fecha_status?:string
    hora_status?:string
    nom_status?:string
    nom_naturaleza?:string
}

export interface Cartaralm
{
    tarifa?:string
    fecha_inicio?:string
    fecha_final?:string
    peso_base?:string
    medida?:string
    valor_base?:string
    peso_adicional?:string
    valor_peso_adic?:string
    status?:string
    nom_status?:string
}

export interface Carinent
{
    tipo?:string
    nom_tipo?:string
    codigo?:string
    descripcion?:string
    status?:string
    nom_status?:string
}

export interface Cartari
{
    tarifa?:string
    fecha_inicio?:string
    fecha_final?:string
    entrada?:string
    costo_diario?:string
    medida?:string
    minimo_diario?:string
    full_pallet?:string
    status?:string
    nom_status?:string   
}

export interface Logubica
{
    ubicacion?:string
    almacen?:string
    area?:string
    anaquel?:string
    cara?:string
    fila?:string
    columna?:string
    status?:string
    nom_status?:string
}

export interface Logarea
{
    almacen?:string
    nom_almacen?:string
    area?:string
    descripcion?:string
    status?:string
    nom_status?:string
}

export interface Loganaquel
{
    almacen?:string
    area?:string
    anaquel?:string
    cara?:string
    status?:string
    nom_status?:string
}

export interface Logalma
{
    almacen?:string
    descripcion?:string
    status?:string
    nom_status?:string
}

export interface Carcmani
{
    fecha?:string
    operador?:string
    nom_operador?:string
    numero_vuelo?:string
    puerto_despacho?:string
    nom_pto_despacho?:string
    puerto_destino?:string
    nom_pto_destino?:string
    tot_piezas?:string
    peso_kg?:string
    aeronave?:string
    nom_aeronave?:string
    matricula?:string
    status?:string
    nom_status?:string
}

export interface Cardmani
{
    secuencia?:string
    no_embarque?:string
    naturaleza?:string
    nom_naturaleza?:string
    cant_items?:string
    peso_kg?:string
    remitente?:string
    destinatario?:string
    comentarios?:string
    ubicacion?:string
    status?:string
    nom_status?:string
}