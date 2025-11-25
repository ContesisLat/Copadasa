<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <hr>
        <div class="col-10 d-flex flex-column justify-content-center align-items-center" style="gap: 50px;">
            <div class="row">
                <form>
                    <h3>Ingreso Cuarto Frío</h3>
                    <div class="row mb-1">
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Fecha</label>
                        <div class="col-sm-3">
                            <input type="text" v-model="formDataI.fecha" class="form-control" id="validationCustom01" required disabled>
                        </div> 
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Llegada</label>
                        <div class="col-sm-3">
                            <input type="date" v-model="formDataI.fecha_llegada" id="validationCustom01"  required>
                        </div>
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Hora</label> 
                        <div class="col-md-2">
                            <input type="time" v-model="formDataI.hora_llegada"  id="validationCustom02"  required>
                        </div>
                    </div>
                    <div class="row mb-1">
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Transac.</label>
                        <div class="col-sm-3">
                            <select class="form-select form-select-sm" v-model="formDataI.codigo" >
                                <option selected>{{ descripcionCodigo }}</option>
                                <option v-for="op in codigos" :key="op.codigo" :value="op.codigo">{{ op.descripcion }}</option>
                            </select>
                        </div> 
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Docto.</label> 
                        <div class="col-md-3">
                            <input type="text" v-model="formDataI.documento" class="form-control" id="validationCustom01" required disabled>   
                        </div>
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Guía</label>
                        <div class="col-md-2">
                            <input class="form-control form-control-sm" type="text" v-model="formDataI.guia">
                        </div>
                    </div>
                    <div class="row mb-1"> 
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Cliente</label>
                        <div class="col-md-7">
                            <select class="form-select form-select-sm" v-model="formDataI.cliente" >
                                <option selected>{{ descripcionCliente }}</option>
                                <option v-for="op in clientes" :key="op.cliente" :value="op.cliente">{{ op.nombre_comercial }}</option>
                            </select>
                        </div>
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Estado</label>
                        <div class="col-md-3">
                            <select class="form-select" v-model="formDataI.status" id="validationCustom04" required disabled >
                                <option value="I">Ingreso</option>
                                <option value="D">Despachado</option>
                            </select>
                        </div>
                    </div>
                    <div class="row mb-1"> 
                        <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Comentario</label> 
                        <div class="col-md-9">
                            <input type="text" v-model="formDataI.comentario" class="form-control" id="validationCustom01" required>   
                        </div>
                    </div>
                </form>
            </div>
            <div class="row"> <!--Arreglo-->
                <div class="div-dotted">
                    <form>
                        <div class="row g-3 mb-2" v-for="(registro, index) in registros" :key="index">
                            <div class="col-md-1">
                                <input v-model="registro.secuencia" type="text" class="form-control form-control-sm"
                                    id="validationDefault03" placeholder="Sec." disabled>
                            </div>
                            <div class="col-md-2">
                                <input v-model="registro.orden_produccion" type="text" class="form-control form-control-sm"
                                    id="validationDefault03" placeholder="No. Pallet" >
                            </div>
                            <div class="col-md-2">
                                <input v-model="registro.pallets" type="text" class="form-control form-control-sm"
                                id="validationDefault02" placeholder="Pallets" >
                            </div>
                            <div class="col-md-2">
                                <input v-model="registro.cajas" type="text" class="form-control form-control-sm"
                                id="validationDefault02" placeholder="Cajas" >
                            </div>
                            <div class="col-md-2">
                                <input v-model="registro.peso" type="text" class="form-control form-control-sm"
                                id="validationDefault02" placeholder="Peso" >
                            </div>
                            <div class="col-md-2">
                                <select class="form-select" v-model="registro.status" id="validationCustom04" required disabled >
                                    <option value="A">Activo</option>
                                    <option value="I">Inactivo</option>
                                </select> 
                            </div>
                        </div>
                    </form>
                </div>
              </div>
            <div class="col-12">
                <button class="btn btn-secondary me-2" type="button" style="background-color: #24292F;" @click="handleClick">Cancelar</button>
                <button class="btn btn-primary" type="button" style="background-color: #001982;" @click="handleSubmit">Enviar</button>
            </div>
        </div>
    </div> 
</template>

<script lang="ts" setup>
import { defineProps,defineEmits,Ref,ref, computed, watch, onMounted } from 'vue'
import axios from 'axios';
import { useDateTimeStore } from '@/store/dateTimeStore';
import { userGlobalStore } from '@/store/userGlobal';
import { UrlGlobal } from '@/store/dominioGlobal';
import { useAlert } from '@/store/useAlert';
import LogTral from '../LogTral.vue';
 
const { success, error, question, warning } = useAlert()

const dUrl = UrlGlobal()
const dateTimeStore = useDateTimeStore();
const userStore = userGlobalStore();



//variables reactivas para los campos del formulario
//const fecha = ref<string>('')
//const status = ref<string>('')
//const fecha_llegada = ref<string>('')
//const hora_llegada = ref<string>('')
//const codigo = ref<string>('')
//const guia = ref<string>('')
//const documento = ref<string>('')
//const cliente = ref<string>('')

let fila = 1
//props y emits----------------------------------------------------------------
const props = defineProps({
    btnIn: Boolean,
    fecha: String
     
})
const emits = defineEmits(['insertProps'])
        const handleClick = () =>{
            emits("insertProps",!props.btnIn)
            
        }
//----------------------------------------------------------------
// Valida Array
function valida(arr: string[]): boolean {
  let valido = true
  const uniqueElement = new Set(arr)
  if (arr.length != uniqueElement.size) {
    valido = false
  }

  return valido
}

let fecha = ref(props.fecha)
let docto: string

// envio del insert a la tabla en la base de datos a traves de la api en django
const handleSubmit = async () =>{
    dateTimeStore.refreshDateTime();
    
// VALIDACIONES
    if(!formDataI.value.fecha) {
        error('No tiene fecha la transacción... ')
        return
    }

    const fecha_i = new Date(formDataI.value.fecha)
    const fecha_f = new Date(formDataI.value.fecha_llegada)

    if(fecha_f > fecha_i) {
        error('Fecha de Llegada no puede ser mayor a la fecha... ')
        return
    }
    //if(!formDataI.value.documento) {
    //    error('Digite el documento de movimiento... ')
    //    return
    //}
    if(!formDataI.value.guia) {
        error('Digite la guía de movimiento... ')
        return
    }
   
    if(!formDataI.value.codigo) {
        console.log(formDataI.value.codigo)
        error('Escoja la transacción... ')
        return
    }
    if (!formDataI.value.cliente) {
        error('Digite el cliente propietario de la mercancía... ')
        return
    }
    if(!formDataI.value.comentario) {
        error('Digite los comentarios del ingreso... ')
        return
    }
// VALIDA ARRAY
     
    const guiaArray: (string | null)[]= registros.value.map(item => item.orden_produccion)
  
    const arrayFn = guiaArray.filter((item): item is string => item !=null)

    let resultado: boolean = valida(arrayFn);
    if (!resultado) {
        error('Existen números de pallets repetidos... ')
        return
    }
// VALIDA CONTENIDO DEL ARRAY
    let indice = registros.value.length -1
    for (let i = 0; i < indice; i++) {
        const arreglo = registros.value[i]
        let pallets = Number(arreglo.pallets)
        let peso = Number(arreglo.peso)
        let cajas = Number(arreglo.cajas)
        if (typeof arreglo.orden_produccion !== 'string' || arreglo.orden_produccion.trim() === '') {
            error (`Error: Falta el número de Pallet en la posición ${arreglo.secuencia}`)
            return
        }
        if (typeof pallets !== 'number' || pallets < 0) {
            error (`Error: Campo cantidad de Pallets es incorrecto en la secuencia ${arreglo.secuencia}`)
            return
        }
        if (typeof cajas !== 'number' || cajas < 0) {
            error (`Error: Campo cantidad de Cajas es incorrecto en la secuencia ${arreglo.secuencia}`)
            return
        }
        if (pallets == 0 && cajas == 0) {
            error (`Error: Pallets o Cajas deben tener valor en la secuencia ${arreglo.secuencia}`)
            return
        }
        if (typeof peso !== 'number' || peso <= 0 || peso == undefined) {
            error (`Error: Campo peso es incorrecto en la secuencia ${arreglo.secuencia}`)
            return
        }
    }

// VALIDA QUE GUÍA POR CLIENTE NO SE REPITA
    try {
        const response = await axios.post(dUrl.urlGlobal + '/api2/query', { tabla: 'logctmo', 
            filtro: { compania:'300', agencia: '001', fecha: formDataI.value.fecha, almacen: '02', 
                cliente: formDataI.value.cliente, guia_despacho: formDataI.value.guia }});

        dataList.value = response.data;

        if (dataList.value.length > 0) {
        warning('Al Cliente ya se le registro esta guía en el almacén', 'Valide la Información a Registrar')
        return
        }

    } catch (err: any) {
        error(err.response?.data?.detail || 'Ocurrió un error en la consulta.')
    }

    const result = await question(
    'Se va a insertar el campo con los nuevos datos.',
    '¿Deseas insertar este registro?'
    )

    if (!result.isConfirmed) {
        return
    }

    //registros.value.pop()
    registros.value.length = registros.value.length -1

    const data = {
        model:"logctmo",
        data:{
            compania: '300',
            agencia: '001',
            fecha: formDataI.value.fecha,
            almacen: '02',
            codigo: formDataI.value.codigo,
            documento: formDataI.value.documento,
            creado_por:userStore.globalUser,
            fecha_creado: dateTimeStore.formattedDate,
            hora_creado: dateTimeStore.formattedTime,
            guia_despacho: formDataI.value.guia,
            cliente: formDataI.value.cliente,
            fecha_llegada: formDataI.value.fecha_llegada,
            hora_llegada: formDataI.value.hora_llegada,
            comentario: formDataI.value.comentario,
            status: formDataI.value.status,
                  
        }
    }
    
    try { 
        const response = await fetch(dUrl.urlGlobal +'/api2/insert/',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        if(response.ok){
            const responseData = await response.json()

            console.log("Insercion exitosa:",responseData)
        
            try {
                const response = await axios.post(dUrl.urlGlobal + '/api2/query', { tabla: 'carussec', 
                    filtro: { usuario: userStore.globalUser, tabla: 'logctmo' }});

                dataList.value = response.data;
                docto = dataList.value[0].secuencia

            } catch(err: any) {
                error('NO se pudo accesar el secuencial de almacen')
            }
            
// INSERT DEL ARRAY
            
            for (const fila of registros.value) {
            const data = {
            model: "logdemo",
            data: {
                compania: '300',
                agencia: '001',
                fecha: formDataI.value.fecha,
                almacen: '02',
                codigo: formDataI.value.codigo,
                documento: docto,
                secuencia: fila.secuencia,
                orden_produccion: fila.orden_produccion,
                pallets: fila.pallets,
                peso: fila.peso,
                cajas: fila.cajas,
                unidad: 0,
                creado_por: userStore.globalUser,
                fecha_creado: dateTimeStore.formattedDate,
                hora_creado: dateTimeStore.formattedTime,
                status: formDataI.value.status
                }
            }
            try {
                const response = await fetch(dUrl.urlGlobal + '/api2/insert/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            if (!response.ok) {
            // Puedes registrar el error y seguir con el siguiente
                error(`Error al insertar registro con pallet: ${fila.orden_produccion}`)
                }else{
                //vali++
            }
            } catch (err: any) {
                error(`Error inesperado en el número ${fila.orden_produccion}:`, err)
      }
    }   
// Fin de Insert
            handleClick()
        }else{
            console.error("Error al insertar en la base de datos:",response.statusText)
        }
    }catch (error){
        console.error("error de red:",error)
    }
}
 
// final handle submit
type Registro = {
  secuencia: number | null
  orden_produccion: string | null
  pallets: string| null
  peso: string | null
  cajas: string | null
  status: string
}

// Inicializa con una sola fila vacía
const registros = ref<Registro[]>([
  { secuencia: fila, orden_produccion: '', pallets: '', cajas: '', peso: '', status: 'A' }
])

// Estado del formulario y la data
const formDataI = ref({
  fecha: fecha.value,
  status: 'I',
  guia: '',
  fecha_llegada: dateTimeStore.formattedDate,
  hora_llegada: dateTimeStore.formattedTime, 
  codigo: '',
  documento: '',
  cliente: '',
  comentario: ''

});

// Variables de control
const dataList = ref<any[]>([]); // Lista de datos de la API
//----------------------------------------------------------------------------------------------
const codigos = ref<any[]>([]);
const clientes = ref<any[]>([])
onMounted( async () => {
  const responseN = await axios.get(dUrl.urlGlobal + '/api2/logtral/filter?status=A')
  codigos.value = responseN.data

  const responseC = await axios.get(dUrl.urlGlobal + '/api2/crmclte/filter?status=A')
  clientes.value = responseC.data
})
//computados de las ayudas
const descripcionCodigo = computed(() => {
  const encontrado = codigos.value.find(op => op.codigo === formDataI.value.codigo)
  return encontrado ? encontrado.descripcion : ''
})

const descripcionCliente = computed(() => {
  const encontrado = clientes.value.find(op => op.cliente === formDataI.value.cliente)
  return encontrado ? encontrado.nombre_comercial : ''
})

//control de filas automaticas de la tabla-----------------------------------------------------------------------------------------------------------------

// Función para validar si una fila está completamente llena
const filaLlena = (fila: Registro | undefined | null) => {
  if (!fila) return false;

  return Object.values(fila).every(val => {
    if (typeof val === 'string') {
      return val.trim() !== ''
    }
    if (typeof val === 'number') {
      return !isNaN(val)
    }
    return false
  })
}
// Observar el último elemento y agregar uno nuevo si está lleno
watch(registros, (newVal) => {
  // Evitar errores si el array está vacío
  if (!newVal.length) {
    fila + 1
    registros.value.push({
      secuencia: fila,
      orden_produccion: '',
      pallets: '',
      cajas: '',
      peso: '',
      status: 'A'
    });
    return;
  }

  // Evaluar la última fila
  const ultimaFila = newVal[newVal.length - 1];
  if (filaLlena(ultimaFila)) {
    fila++
    registros.value.push({
      secuencia: fila,
      orden_produccion: '',
      pallets: '',
      cajas: '',
      peso:'',
      status: 'A'
    });
  }
}, { deep: true });
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

svg {
    fill: black;
}

.modal-backdrop {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    /* Fondo oscuro semitransparente */
    z-index: 1050;
    /* Coloca el fondo oscuro por encima de otros elementos */
    @media screen and (max-width:600px){
        width: 500px;     
    }
}

.ReportPage {
    min-height: 62%;
    width: 75%;
    background: whitesmoke;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 5px;
    display: flex;
    justify-content: left;
    align-items: left;
    display: flex;
    flex-direction: column;
    gap: 15px;
    font-family: 'Poppins', sans-serif;
    color: black;
    padding: 15px;
    z-index: 1060; 
    overflow: hidden;
    @media screen and (max-width: 600px){
        overflow: scroll;
        height: 55%;
        width: 95%; 
    }
}

.ReportPage hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 1px 0;
    padding-left: 100%;
}
</style>