<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Actualizar Areas de Almacen</h4>
        <hr>
        <form class="row g-3 needs-validation" novalidate>
            <div class="col-md-2">
                <label for="validationCustom01" class="form-label">Almacen</label>
                <input type="text" class="form-control" id="validationCustom01" v-model="almacen" required disabled>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-2">
                <label for="validationCustom01" class="form-label">Area</label>
                <input type="text" class="form-control" id="validationCustom01" v-model="area" required disabled>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-5">
                <label for="validationCustom02" class="form-label">Descripcion</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="descripcion" required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-3">
                <label for="validationCustom04" class="form-label">Status</label>
                <select class="form-select" id="validationCustom04" required v-model="status">
                    <option value="A">Activo</option>
                    <option value="I">Inactivo</option>
                </select>
                <div class="invalid-feedback">
                    Please select a valid state.
                </div>
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
import { useDateTimeStore } from '@/store/dateTimeStore';
import { UrlGlobal } from '@/store/dominioGlobal';
import { userGlobalStore } from '@/store/userGlobal';
const dateTimeStore = useDateTimeStore();
const userStore = userGlobalStore();

const dUrl = UrlGlobal()

//props y emits ----------------------------------------------------------------
const props = defineProps({
    btnUp: Boolean,
    almacen: String,
    area: String,
    descripcion: String,
    status: String

})
const emits = defineEmits(['updProps'])
const handleClick = () => {
    emits("updProps", !props.btnUp)
}
//------------------------------------------------------------------------------

//variables reactivas para el formulario----------------------------------------
let almacen = ref(props.almacen)
let area = ref(props.area)
let status = ref(props.status)
let descripcion = ref(props.descripcion)
let modificado_por = null
let fecha_status = null
let hora_status = null 
//------------------------------------------------------------------------------

const handleSubmit = async () => {
    try {
        console.log(props.almacen)
        console.log(props.area)
        dateTimeStore.refreshDateTime
        const response = await axios.post(dUrl.urlGlobal +'/api2/update/', {
            table: 'logarea', 
            filters: { almacen: almacen.value, area: area.value}, // Filtro para identificar el registro a actualizar
            data: { almacen: almacen.value, area: area.value, descripcion: descripcion.value, status: status.value, modificado_por:userStore.globalUser, fecha_status:dateTimeStore.formattedDate,
            hora_status:dateTimeStore.formattedTime } // Datos a actualizar
        })
        console.log(response.data)
        emits("updProps", !props.btnUp)
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