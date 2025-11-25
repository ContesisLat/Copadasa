<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <h4>Calculos Generador por Embarque</h4>
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
        </form>
        <div class="col d-flex flex-column justify-content-center align-item-center" >
            <h3><strong>Cargos</strong></h3>
            <div class="card overflow-scroll">
                <table class="table table-hover  table-sm">
                    <thead>
                        <tr>
                            <th>Cargo</th>
                            <th>Monto</th>
                            <th>Estado</th> 
                        </tr>
                    </thead>
                    <!--tbody>
                        <tr v-for="elm in filteredCarga1" :key="elm.tarifa" 
                            :class="{ 'table-primary': elm.id === id_ref }">
                            <td>{{ elm.nom_tarifa }}</td>
                            <td>{{ elm.monto }}</td>
                            <td>{{ elm.nom_status }}</td>
                        </tr>
                    </tbody-->
                </table>  
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { defineProps, defineEmits, Ref, ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { UrlGlobal } from '@/store/dominioGlobal';
import { userGlobalStore } from '@/store/userGlobal';
import { useDateTimeStore } from '@/store/dateTimeStore';
import { Cardeent } from '@/interface/interfaces';
 
const dateTimeStore = useDateTimeStore()
const userStore = userGlobalStore()

const dUrl = UrlGlobal()
//props y emits ----------------------------------------------------------------
const props = defineProps({
    btnCaUp: Boolean,
    fecha: String,
    operador: String,
    numero_vuelo: String,
    nom_operador: String,
    no_embarque: String,
    confirmado: String,
    fecha_confirma: String,
    hora_confirma: String,

})
const emits = defineEmits(['updateCaProps'])
const handleClick = () => {
    emits("updateCaProps", !props.btnCaUp)
}
//------------------------------------------------------------------------------

//variables reactivas para el formulario----------------------------------------
let fecha = ref(props.fecha)
let operador = ref(props.operador)
let numero_vuelo = ref(props.numero_vuelo)
let no_embarque = ref(props.no_embarque)
let id: any
let tarifa: any
let nom_tarifa: any
let monto: any
let status: any
let nom_status: any
let id_ref = String
 
//------------------------------------------------------------------------------
const cardeent = ref<Array<Cardeent>>([])
const getCardeent = (id_no_embarque: any, id_numero_vuelo: any, id_operador: any, id_fecha: any, id: any) => {
        fecha = id_fecha
        operador = id_operador
        numero_vuelo = id_numero_vuelo
        no_embarque = id_no_embarque 
         
        axios.get(`${dUrl.urlGlobal}/api2/cardeent/mostrar?id_no_embarque=${id_no_embarque}&id_numero_vuelo=${id_numero_vuelo}&id_operador=${id_operador}&id_fecha=${id_fecha}`)
        //axios.get(final)    
            .then(response => { //console.log(response.data)
                cardeent.value = response.data;
                console.log(response.data)
                
            })
            .catch(error => {
                console.error('Error buscando detalles de manifiesto:', error);
        });
    }

const filteredCarga1 = () => {
    
    return cardeent.value.filter(elm => {
        return (
            elm.id?.toLocaleLowerCase().valueOf ||
            elm.tarifa?.toLocaleLowerCase().valueOf ||
            elm.monto?.toLocaleLowerCase().valueOf ||
            elm.status?.toLocaleLowerCase().valueOf)
                   
})
}

const handleSubmit = async () => {
     
    emits("updateCaProps", !props.btnCaUp)
    
}

onMounted(() => {
    getCardeent("fecha", "operador", "numero_vuelo", "no_embarque", null);
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

.Card {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 95%;
  height: 95%;
  display: flex;
  border-radius: 10px;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
  font-family: 'Poppins', sans-serif;
  color: white;
  background: linear-gradient(to right, #ccd0cf, #9ba8ab, #4a5c6a);
  overflow: scroll;

  @media screen and (max-width: 600px) {
    overflow: scroll;
  }
}
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