
 export interface Natur{
    naturaleza?:string,
    nombre?:string,
    creado_por?:string,
    fecha_creado?:string,
    hora_creado?:string,
    status?:string,
    modificado_por?:string,
    fecha_status?:string,
    hora_status?:string
}

export interface CargCaman{
    cargo?:string,
    nombre?:string,
    creado_por?:string,
    fecha_creado?:string,
    hora_creado?:string
    naturaleza?:string
    status?:string,
    modificado_por?:string,
    fecha_status?:string,
    hora_status?:string
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
