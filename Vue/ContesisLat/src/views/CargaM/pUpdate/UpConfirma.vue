<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Confirmar No. Embarque</h4>
        <hr>
        <form class="row g-3 needs-validation" novalidate>
            <div class="col-md-2">
                <label for="validationCustom01" class="form-label">Fecha</label>
                <input type="text" class="form-control" id="validationCustom01" v-model="fecha" required disabled>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-3">
                <label for="validationCustom02" class="form-label">operador</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="operador" required disabled>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-3">
                <label for="validationCustom02" class="form-label">numero_vuelo</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="numero_vuelo" required disabled>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-3">
                <label for="validationCustom02" class="form-label">No. Embarque</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="no_embarque" required disabled>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-sm-3">
                <label for="validationCustom02" class="form-label">Confirmado Por</label>
                <input class="form-control form-control-sm" v-model="confirmado" disabled>
            </div>
            <div class="col-sm-3"> 
                <label for="validationCustom02" class="form-label">Fecha Confirmado</label>
                <input class="form-control form-control-sm" type="date" v-model="fecha_confirma">
            </div>
            <div class="col-sm-3">
                <label for="validationCustom02" class="form-label">Hora Confirmado</label>
                <input class="form-control form-control-sm" type="time" v-model="hora_confirma">
            </div>
            <div class="col-12">
                <button class="btn btn-secondary me-2" type="button" style="background-color: #24292F;"
                    @click="handleClick">Cancelar</button>
                <button class="btn btn-primary" type="button" style="background-color: #001982;"
                    @click="handleSubmit">Enviar</button>
            </div>
        </form>
    </div>
</template>

<script lang="ts" setup>
import { defineProps, defineEmits, Ref, ref } from 'vue'
import axios from 'axios'
import { UrlGlobal } from '@/store/dominioGlobal';
import { userGlobalStore } from '@/store/userGlobal';
import { useDateTimeStore } from '@/store/dateTimeStore';
 
const dateTimeStore = useDateTimeStore();
const userStore = userGlobalStore();

const dUrl = UrlGlobal()

//props y emits ----------------------------------------------------------------
const props = defineProps({
    btnUp: Boolean,
    fecha: String,
    operador: String,
    numero_vuelo: String,
    nom_operador: String,
    no_embarque: String,
    confirmado: String,
    fecha_confirma: String,
    hora_confirma: String,

})
const emits = defineEmits(['updateProps'])
const handleClick = () => {
    emits("updateProps", !props.btnUp)
}
//------------------------------------------------------------------------------

//variables reactivas para el formulario----------------------------------------
let fecha = ref(props.fecha)
let operador = ref(props.operador)
let numero_vuelo = ref(props.numero_vuelo)
let no_embarque = ref(props.no_embarque)
let confirmado = userStore.globalUser
let fecha_confirma = dateTimeStore.formattedDate
let hora_confirma = dateTimeStore.formattedTime
//------------------------------------------------------------------------------

const handleSubmit = async () => {
    try {
        console.log(no_embarque.value)
        const response = await axios.post(dUrl.urlGlobal +'/api2/update/', {
            table: 'cardmani', 
            filters: { fecha: fecha.value, operador: operador.value, numero_vuelo: numero_vuelo.value,
                    no_embarque: no_embarque.value }, // Filtro para identificar el registro a actualizar
            data: { confirmado: confirmado, fecha_confirma: fecha_confirma, hora_confirma: hora_confirma,
                status:'L', modificado_por: confirmado, fecha_status: dateTimeStore.formattedDate,
                hora_status: dateTimeStore.formattedTime } // Datos a actualizar
        })
        console.log(response.data)
        emits("updateProps", !props.btnUp)
    } catch (error) {
        console.error("Error actualizando datos:", error)
    }
}
</script>

<style scoped>
svg {
    fill: black;
}

.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    /* Fondo oscuro semitransparente */
    z-index: 1050;
    /* Coloca el fondo oscuro por encima de otros elementos */
    @media screen and (max-width: 600px){
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
    @media screen and (max-width:600px){
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