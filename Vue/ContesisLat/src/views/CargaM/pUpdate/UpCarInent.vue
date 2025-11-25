<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Actualizar Indicadores</h4>
        <hr>
        <form class="row g-3 needs-validation" novalidate>
            <div class="col-md-3">
                <label for="validationCustom04" class="form-label">Tipo</label>
                <select class="form-select" id="validationCustom04" required v-model="tipo">
                    <option value="E">Entrega</option>
                    <option value="E">Despacho</option>
                </select>
                <div class="invalid-feedback">
                    Please select a valid state.
                </div>
            </div>
            <div class="col-md-2">
                <label for="validationCustom02" class="form-label">Codigo</label>
                <input type="text" v-model="codigo" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-4">
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
import { UrlGlobal } from '@/store/dominioGlobal';

const dUrl = UrlGlobal()

//props y emits ----------------------------------------------------------------
const props = defineProps({
    btnUp: Boolean,
    tipo: String,
    codigo: String,
    descripcion: String,
    status: String

})
const emits = defineEmits(['updateProps'])
const handleClick = () => {
    emits("updateProps", !props.btnUp)
}
//------------------------------------------------------------------------------

//variables reactivas para el formulario----------------------------------------

let tipo = ref(props.tipo)
let codigo = ref(props.codigo)
let descripcion = ref(props.descripcion)
let status = ref(props.status)
//------------------------------------------------------------------------------


const handleSubmit = async () => {
    try {
        const response = await axios.post(dUrl.urlGlobal +'/api2/update/', {
            table: 'carinent', 
            filters: { tipo: tipo.value, codigo: codigo.value}, // Filtro para identificar el registro a actualizar
            data: { codigo: codigo.value, descripcion: descripcion.value, status: status.value } // Datos a actualizar
        })
        console.log(response.data)
        emits("updateProps", !props.btnUp)
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