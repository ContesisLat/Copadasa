<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Tarifas de Refrigeración</h4>
        <hr>
        <form class="row g-3 needs-validation" novalidate>
            <div class="col-md-2">
                <label for="validationCustom01" class="form-label">Inicio</label>
                <input type="date" v-model="fecha_inicio" class="form-control" id="validationCustom01" required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-2">
                <label for="validationCustom02" class="form-label">Final</label>
                <input type="date" v-model="fecha_final" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-1">
                <label for="validationCustom02" class="form-label">Entrada</label>
                <input type="text" v-model="entrada" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-1">
                <label for="validationCustom04" class="form-label">U/medida</label>
                <select class="form-select" v-model="medida" id="validationCustom04" required >
                    <option value="Kilos">Kilos</option>
                    <option value="Libras">Libras</option>
                </select>
            </div>
            <div class="col-md-1">
                <label for="validationCustom02" class="form-label">Peso/Base</label>
                <input type="text" v-model="peso_base" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-1">
                <label for="validationCustom02" class="form-label">Costo/Diario</label>
                <input type="text" v-model="costo_diario" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-1">
                <label for="validationCustom02" class="form-label">Min/Dia</label>
                <input type="text" v-model="minimo_diario" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-1">
                <label for="validationCustom02" class="form-label">F/Pallet</label>
                <input type="text" v-model="full_pallet" class="form-control" id="validationCustom02"  required>
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
import { defineProps,defineEmits,Ref,ref } from 'vue'
import { useDateTimeStore } from '@/store/dateTimeStore';
import { userGlobalStore } from '@/store/userGlobal';
import { UrlGlobal } from '@/store/dominioGlobal';
import { useAlert } from '@/store/useAlert';
const { success, error, question, warning } = useAlert()


const dUrl = UrlGlobal()
const dateTimeStore = useDateTimeStore();
const userStore = userGlobalStore();

//variables reactivas para los campos del formulario
const fecha_inicio = ref<string>('')
const fecha_final = ref<string>('')
const entrada = ref<string>('')
const medida = ref<string>('')
const peso_base = ref<string>('')
const costo_diario = ref<string>('')
const minimo_diario = ref<string>('')
const full_pallet = ref<string>('')
const status = ref<string>('')

//props y emits----------------------------------------------------------------
const props = defineProps({
    btnIn: Boolean,
})
const emits = defineEmits(['insertProps'])
        const handleClick = () =>{
            emits("insertProps",!props.btnIn)
        }
//----------------------------------------------------------------

// envio del insert a la tabla en la base de datos a traves de la api en django
const handleSubmit = async () =>{
    if (fecha_inicio.value > fecha_final.value) {
        error('Fecha Inicial no puede ser mayor que Fecha Final...')
        return
    }
    const ent = Number(entrada.value)
    if (typeof ent !== 'number') {
        error('Información incorrecta en Costo Entrada...')
        return
    }
    if (ent == 0 || ent < 0) {
        error('Información inválida en Costo de Etrada')
        return
    }
    const peso = parseFloat(peso_base.value)
    if (typeof peso !== 'number') {
        error('Información incorrecta en Peso Base...')
        return
    }
    if (peso == 0 || peso < 0) {
        error('Valor de Peso Base es incorrecto...')
        return
    }
    const costo = parseFloat(costo_diario.value)  
    if (typeof costo !== 'number') {
        error('Información de Costo Diario incorrecta...')
        return
    }
    if (costo == 0 || costo < 0) {
        error('Error en el Costo Diario...')
        return
    }
    const minimo = parseFloat(costo_diario.value)
    if (typeof minimo !== 'number') {
        error('Información Mínimo Diario es incorrecta...')
        return
    } 
    if (minimo == 0 || minimo < 0) {
        error('Valor de Mínimo Diario es incorrecto...')
        return
    }
    const fpallet = parseFloat(full_pallet.value)
    if (typeof fpallet !== 'number') {
        error('Información del Full Pallet incorrecta...')
        return
    }
    if (fpallet == 0 || fpallet < 0) {
        error('Información Full Pallet incorrecta...')
        return
    }

    const result = await question(
    'Se va a insertar el campo con los nuevos datos.',
    '¿Deseas insertar este registro?'
    )

    if (!result.isConfirmed) {
        return
    }
    dateTimeStore.refreshDateTime();
    console.log(dateTimeStore.formattedDate)
    const data = {
        model:"cartari",
        data:{
            tarifa: '03',
            fecha_inicio:fecha_inicio.value,
            fecha_final: fecha_final.value,
            creado_por:userStore.globalUser,
            fecha_creado:dateTimeStore.formattedDate,
            hora_creado:dateTimeStore.formattedTime,
            entrada: entrada.value,
            peso_base: peso_base.value,
            costo_diario: costo_diario.value,
            medida: medida.value,
            minimo_diario: minimo_diario.value,
            full_pallet: full_pallet.value,
            status:status.value,
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
//----------------------------------------------------------------------------------------------
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