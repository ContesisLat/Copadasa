<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Tarifas Servicios Aéreos</h4>
        <hr>
        <form class="row g-3 needs-validation" novalidate>
            <div class="col-md-2">
                <label for="validationCustom01" class="form-label">Fecha Inicio</label>
                <input type="date" v-model="fecha_inicio" class="form-control" id="validationCustom01" required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-2">
                <label for="validationCustom02" class="form-label">Fecha Final</label>
                <input type="date" v-model="fecha_final" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-3">
                <label for="validationCustom02" class="form-label">Cargo</label>
                <select class="form-select form-select-sm" v-model="cargo" :disabled= false>
                    <option selected>{{ descripcionCargos(idncargo)}}</option>
                    <option v-for="i in cargos" :key="i.cargo"  :value="i.cargo" @click="idN(i.cargo)">{{ i.nombre }}</option>
                </select>
            </div>
            <div class="col-md-2">
                <label for="validationCustom02" class="form-label">Costo Hora</label>
                <input type="number" v-model="costo_hora" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-2">
                <label for="validationCustom04" class="form-label">Status</label>
                <select class="form-select" v-model="status" id="validationCustom04" required >
                    <option value="A">Activo</option>
                    <option value="I">Inactivo</option>
                </select>
                <div class="invalid-feedback">
                    Please select a valid state.
                </div>
            </div>
            <div class="col-12">
                <button class="btn btn-secondary me-2" type="button" style="background-color: #24292F;" @click="handleClick">Cancelar</button>
                <button class="btn btn-primary" type="button" style="background-color: #001982;" @click="handleSubmit">Enviar</button>
            </div>
        </form>

    </div> 
</template>

<script lang="ts" setup>
import { defineProps,defineEmits,Ref,ref, onMounted } from 'vue'
import axios from 'axios'
import { useDateTimeStore } from '@/store/dateTimeStore';
import { userGlobalStore } from '@/store/userGlobal';
import { UrlGlobal } from '@/store/dominioGlobal';
import { useAlert } from '@/store/useAlert';
const { error, question, success, warning } = useAlert()

const dUrl = UrlGlobal()
const dateTimeStore = useDateTimeStore();
const userStore = userGlobalStore();

//variables reactivas para los campos del formulario
const fecha_inicio = ref<string>('')
const fecha_final = ref<string>('')
const cargo = ref<string>('')
const costo_hora = ref<string>('')
const status = ref<string>('') 

//props y emits----------------------------------------------------------------
const props = defineProps({
    btnTvIn: Boolean,
    aeronave: String
})
const emits = defineEmits(['insTvProps'])
        const handleClick = () =>{
            emits("insTvProps",!props.btnTvIn)
        }
//----------------------------------------------------------------
// Variables reactivas
status.value = 'A'

// envio del insert a la tabla en la base de datos a traves de la api en django
const handleSubmit = async () =>{
    if (!fecha_inicio.value) {
        error('Digite la fecha de inicio de la vigencia...')
        return
    }
    if (!fecha_final.value) {
        error('Digite la fecha final de la vigencia...')
        return
    }
    if (fecha_inicio.value > fecha_final.value) {
        error('Fecha de Inicio no puede ser mayor a la Fecha Final...')
        return
    }
    if (!cargo.value) {
        error('Tiene que digitar el campo correspondiente...')
        return
    }
    if (typeof costo_hora.value !='number') {
        error ('Información de costo por hora incorrecto...')
        return
    }

    dateTimeStore.refreshDateTime();
    console.log(dateTimeStore.formattedDate)
    const data = {
        model:"cartarvue",
        data:{
            aeronave: props.aeronave,
            fecha_inicio:fecha_inicio.value,
            fecha_final: fecha_final.value,
            cargo: cargo.value,
            creado_por:userStore.globalUser,
            fecha_creado:dateTimeStore.formattedDate,
            hora_creado:dateTimeStore.formattedTime,
            costo_Hora: costo_hora.value,
            status:status.value
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
            handleClick()
        }else{
            console.error("Error al insertar en la base de datos:",response.statusText)
        }
    }catch (error){
        console.error("error de red:",error)
    }
}
const cargos = ref<any[]>([]);
onMounted(async () => {
     const responseN = await axios.get(dUrl.urlGlobal + '/api2/caratenvue/filter?status=A')
  cargos.value = responseN.data
})

const descripcionCargos = (cargosId: string) => {
  const encontrado = cargos.value.find(i => i.cargo === cargosId)
  return encontrado ? encontrado.nombre : ''
}
let idncargo : any
const idN = (naturalezaId: string) => {
  idncargo = naturalezaId
}

//----------------------------------------------------------------------------------------------
</script>

<style scoped>
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
    font-family: Trebuchet MS;
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