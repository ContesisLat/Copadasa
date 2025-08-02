<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Actualiza Tarifas Refrigeración</h4>
        <hr>
        <form class="row g-3 needs-validation" novalidate>
            <div class="col-md-2">
                <label for="validationCustom01" class="form-label">Entrada</label>
                <input type="text" class="form-control" id="validationCustom01" v-model="entrada" required >
            </div>
            <div class="col-md-2">
                <label for="validationCustom02" class="form-label">Peso Base</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="peso_base" required>
            </div>
            <div class="col-md-2">
                <label for="validationCustom02" class="form-label">Diario</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="costo_diario" required>
            </div>
            <div class="col-md-2">
                <label for="validationCustom02" class="form-label">Mínimo</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="minimo_diario" required>
            </div>
            <div class="col-md-2">
                <label for="validationCustom02" class="form-label">F Pallet</label>
                <input type="text" class="form-control" id="validationCustom02" v-model="full_pallet" required>
            </div>
            <div class="col-md-2">
                <label for="validationCustom04" class="form-label">Status</label>
                <select class="form-select" id="validationCustom04" required v-model="status" disabled>
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
    fecha_inicio: String,
    fecha_final: String,
    entrada: String,
    medida: String,
    peso_base: String,
    costo_diario: String,
    minimo_diario: String,
    full_pallet: String,
    status: String,
    id_ref: String

})
const emits = defineEmits(['updateProps'])
const handleClick = () => {
    emits("updateProps", !props.btnUp)
}
//------------------------------------------------------------------------------

//variables reactivas para el formulario----------------------------------------
const fecha_inicio = ref(props.fecha_inicio)
const entrada = ref(props.entrada)
const peso_base = ref(props.peso_base)
const costo_diario = ref(props.costo_diario)
const minimo_diario = ref(props.minimo_diario)
const full_pallet = ref(props.full_pallet)
const status = ref(props.status)
const id_ref = ref(props.id_ref)
//------------------------------------------------------------------------------

const handleSubmit = async () => {
    try {
        const response = await axios.post(dUrl.urlGlobal +'/api2/update/', {
            table: 'cartari', 
            filters: { tarifa: "03", fecha_inicio: fecha_inicio.value}, // Filtro para identificar el registro a actualizar
            data: { entrada: entrada.value, costo_diario: costo_diario.value, minimo_diario: minimo_diario.value,
                full_pallet: full_pallet.value, peso_base: peso_base.value, status: status.value } // Datos a actualizar
        })
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