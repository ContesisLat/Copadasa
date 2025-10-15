<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Agregar Tarifas de Almacenaje</h4>
        <hr>
        <form class="row g-3 needs-validation" novalidate>
            <div class="col-md-2">
                <label for="validationCustom01" class="form-label">F. Inicio</label>
                <input type="date" v-model="fechaInicio" class="form-control" id="validationCustom01" required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-2">
                <label for="validationCustom02" class="form-label">F. Final</label>
                <input type="date" v-model="fechaFinal" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-1">
                <label for="validationCustom02" class="form-label">P Base</label>
                <input type="text" v-model="pesoBase" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-2">
                <label for="validationCustom04" class="form-label">Medida</label>
                <select class="form-select" v-model="medida" id="validationCustom04" required >
                    <option value="Kilos">Kilos</option>
                    <option value="Libras">Llibras</option>
                </select>
            </div>
            <div class="col-md-1">
                <label for="validationCustom02" class="form-label">V. Base</label>
                <input type="text" v-model="valorBase" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
             <div class="col-md-1">
                <label for="validationCustom02" class="form-label">P Adic</label>
                <input type="text" v-model="pesoAdic" class="form-control" id="validationCustom02"  required>
                <div class="valid-feedback">
                    Looks good!
                </div>
            </div>
            <div class="col-md-1">
                <label for="validationCustom02" class="form-label">VP Ad.</label>
                <input type="text" v-model="valPesoAdic" class="form-control" id="validationCustom02"  required>
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
const fechaInicio = ref<string>('')
const fechaFinal = ref<string>('')
const pesoBase = ref<string>('')
const medida = ref<string>('')
const valorBase = ref<string>('')
const pesoAdic = ref<string>('')
const valPesoAdic = ref<string>('')
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

    if (fechaInicio.value > fechaFinal.value) {
        error('Fecha de inicio es mayor que la Fecha Final...')
        return
    }
    const peso = Number(pesoBase.value)
    if(typeof peso !== 'number') {
        error('Información inválida en Peso Base...')
        return
    }
    if (peso == 0 || peso < 0) {
        error('Digite un monto válido en el Peso Base')
    }
    const valorB = Number(valorBase.value)
    if (typeof valorB !== 'number') {
        error('Información inválida en Valor Base...')
        return
    }
    if (valorB == 0  || valorB < 0) {
        error('Información incorrecta en Valor Base...')
    }
    const pesoA =Number(pesoAdic)
    if (typeof pesoA !== 'number') {
        error('Información incorrecta en Peso Adicional...')
        return
    }
    if (pesoA == 0 || pesoA < 0) {
        error ('Información incorrecta en Peso Adicional...')
        return
    }
    const ValPA = Number(valPesoAdic)
    if (typeof ValPA !== 'number') {
        error('Valor del Peso Adicional incorrecto...')
        return
    }
    if (ValPA == 0 || ValPA < 0) {
        error('Información del Valor por Peso Adicional incorrecta...')
        return
    }
    if (!status.value) {
        error('Estado del Registro no puede ser nulo...')
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
        model:"cartaralm",
        data:{
            tarifa: '01',
            fecha_inicio: fechaInicio.value,
            fecha_final: fechaFinal.value,
            medida: medida.value,
            peso_base: pesoBase.value,
            valor_base: valorBase.value,
            peso_adicional: pesoAdic.value,
            valor_peso_adic: valPesoAdic.value,
            creado_por:userStore.globalUser,
            fecha_creado:dateTimeStore.formattedDate,
            hora_creado:dateTimeStore.formattedTime,
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