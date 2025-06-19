<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Eliminar CarNatur</h4>
        <hr>
        <div class="modal-body">
            <p>¿Estás seguro de querer eliminar el registro {{ (almacen, area, anaquel, cara, fila, columna) }}?</p>
            <p>Esta acción no se puede deshacer.</p>
        </div>
        <hr>
        <div class="group-btn">
            <button class="btn btn-secondary me-2" type="button" style="background-color: #24292F;"
                @click="handleClick">Cancelar</button>
            <button class="btn btn-primary" type="button" style="background-color: #001982;"
                @click="handleSubmit">Eliminar</button>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { defineProps, defineEmits, Ref, ref } from 'vue'
import axios from 'axios';
import { UrlGlobal } from '@/store/dominioGlobal';

const dUrl = UrlGlobal()
//props y emits ----------------------------------------------------------------
const props = defineProps({
    btnLuDl: Boolean,
    almacen: String,
    area: String,
    anaquel: String,
    cara: String,
    fila: String,
    columna: String,

})
const emits = defineEmits(['delLuProps'])
const handleClick = () => {
    emits("delLuProps", !props.btnLuDl)
}
//----------------------------------------------------------------

// variable para el parametro o filtro para eliminar---------------------------
let almacen = ref(props.almacen)
let area = ref(props.area)
let anaquel = ref(props.anaquel)
let cara = ref(props.cara)
let fila = ref(props.fila)
let columna = ref(props.columna)


// función para eliminar el registro---------------------------------------------
const handleSubmit = async () => {
    try {
        const response = await axios.post(dUrl.urlGlobal +'/api2/delete/', {
            table: 'logubica', 
            filters: { almacen: almacen.value, area: area.value, anaquel: anaquel.value, cara: cara.value, fila: fila.value, columna: columna.value
             }, // Filtro para identificar el registro a eliminar
        })
        console.log(response.data)
        emits("delLuProps", !props.btnLuDl)
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
    height: 62%;
    width: 85%;
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
    }
}

.ReportPage hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 1px 0;
    padding-left: 100%;
}

.group-btn{
    justify-content: right;
    align-items: right;
    flex-direction: row;
    display: flex;
}
</style>