<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Actualizar Filas y Columnas</h4>
        <hr>
        <form class="row g-3 needs-validation" novalidate>
            <div class="col-md-4">
                <label for="validationCustom02" class="form-label">Fila</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="fila" required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-4">
                <label for="validationCustom02" class="form-label">Columna</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="columna" required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-4">
                <label for="validationCustom02" class="form-label">Ubicacion</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="ubicacion" required disabled>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-3">
                <label for="validationCustom04" class="form-label">Status</label>
                <select class="form-select" id="validationCustom04" required v-model="status">
                    <option value="A">Activo</option>
                    <option value="B">Inactivo</option>
                </select>
                <div class="invalid-feedback">
                    Please select a valid state.
                </div>
            </div>
            <div class="col-12">
                <button class="btn btn-secondary me-2" type="button" style="background-color: #24292F;"
                    @click="handleClick()">Cancelar</button>
                <button class="btn btn-primary" type="button" style="background-color: #001982;"
                    @click="handleSubmit">Enviar</button>
            </div>
        </form>
    </div>
</template>

<script lang="ts" setup>
import { defineProps, defineEmits, Ref, ref } from 'vue'
import { useDateTimeStore } from '@/store/dateTimeStore';
import axios from 'axios'
import { UrlGlobal } from '@/store/dominioGlobal';
import { userGlobalStore } from '@/store/userGlobal';
import { FileWatcherEventKind } from 'typescript';

const dateTimeStore = useDateTimeStore();
const userStore = userGlobalStore();

const dUrl = UrlGlobal()

//props y emits ----------------------------------------------------------------
const props = defineProps({
    btnLuUp: Boolean,
    almacen: String,
    area: String,
    anaquel: String,
    cara: String,
    fila: String,
    columna: String,
    ubicacion: String,
    status: String,
    
})

const emits = defineEmits(['updLuProps'])
const handleClick = () => {
    emits("updLuProps", !props.btnLuUp)
}
//------------------------------------------------------------------------------

//variables reactivas para el formulario----------------------------------------
const almacen = ref(props.almacen)
const area = ref(props.area)
const anaquel = ref(props.anaquel)
const cara = ref(props.cara)
const fila = ref(props.fila)
const columna = ref(props.columna)
const status = ref(props.status)
const ubicacion = ref(props.ubicacion)

let wcolumna = columna.value
let wfila = fila.value
 

//------------------------------------------------------------------------------
const handleSubmit = async () => {
    try {
        const response = await axios.post(dUrl.urlGlobal +'/api2/update/', {
            table: 'logubica', 
            filters: { almacen: props.almacen, area: props.area, anaquel: props.anaquel, cara: props.cara, fila: wfila, columna: wcolumna}, // Filtro para identificar el registro a actualizar
            data: { fila: fila.value, columna: columna.value, status: status.value, modificado_por:userStore.globalUser, fecha_status:dateTimeStore.formattedDate,
            hora_status:dateTimeStore.formattedTime } // Datos a actualizar
        })
        console.log(response.data)
        emits("updLuProps", !props.btnLuUp)
    } catch (error) {
        console.error("Error actualizando datos:", error)
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

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
    font-family: 'Poppins', sans-serif;
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