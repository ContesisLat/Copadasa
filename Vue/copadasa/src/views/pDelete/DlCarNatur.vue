<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Eliminar CarNatur</h4>
        <hr>
        <div class="modal-body">
            <p>¿Estás seguro de querer eliminar el registro {{ natur }}?</p>
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

//props y emits ----------------------------------------------------------------
const props = defineProps({
    btnDl: Boolean,
    natur: String,
})
const emits = defineEmits(['deleteProps'])
const handleClick = () => {
    emits("deleteProps", !props.btnDl)
}
//----------------------------------------------------------------

// variable para el parametro o filtro para eliminar---------------------------
let natur = ref(props.natur)


// función para eliminar el registro---------------------------------------------
const handleSubmit = async () => {
    try {
        const response = await axios.post('http://103.23.61.168/api2/delete/', {
            table: 'carnatur', 
            filters: { naturaleza: natur.value }, // Filtro para identificar el registro a eliminar
        })
        console.log(response.data)
        emits("deleteProps", !props.btnDl)
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