<template>

    <body>
        <div class="Card">
            <section class="layout">
                <div class="header">
                </div>
                <div class="container">
                    <div class="row">
                        <div class="col d-flex flex-column justify-content-center align-items-center">
                            <h3><strong>Cargos por Manejo</strong></h3>
                            <div class="card overflow-scroll">
                                <table class="table table-hover  table-sm">
                                    <thead>
                                        <tr>
                                            <th>Cargo</th>
                                            <th>Descripción</th>
                                            <th>Tipo</th>
                                            <th>Estado</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="elm in cargcaman" :key="elm.cargo"
                                            @click="getVigencias('02', elm.cargo, elm.nombre, elm.tipo, elm.status)"
                                            :class="{ 'table-primary': elm.cargo === cargoRef }">
                                            <td>{{ elm.cargo }}</td>
                                            <td>{{ elm.nombre }}</td>
                                            <td>{{ elm.nom_tipo}}</td>
                                            <td>{{ elm.nom_status }}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div class="btn-group">
                        <button class="btn-insert" @click.prevent="CbtnIn">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-upload" viewBox="0 0 16 16">
                                <path
                                    d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5" />
                                <path
                                    d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708z" />
                                </svg>
                        </button>
                        <button class="btn-update" @click.prevent="CbtnUp">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-pencil-square" viewBox="0 0 16 16">
                                <path
                                    d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                                <path fill-rule="evenodd"
                                    d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z" />
                            </svg>
                        </button>
                        <button class="btn-delete" @click.prevent="CbtnDl">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-trash3" viewBox="0 0 16 16">
                                <path
                                    d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5" />
                            </svg>
                        </button>
                    </div>
                    <div class="row">
                        <div class="col d-flex flex-column justify-content-center align-items-center">
                            <h3><strong>Tarifas Por Cargos</strong></h3>
                            <div class="card overflow-scroll">
                                <table class="table table-hover  table-sm">
                                    <thead>
                                        <tr>
                                            <th>Fecha Inicio</th>
                                            <th>Fecha Final</th>
                                            <th>Valor</th>
                                            <th>Aplica</th>
                                            <th>Estado</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="elm in cartarman" :key="elm.cargo">
                                            <td>{{ elm.fecha_inicio }}</td>
                                            <td>{{ elm.fecha_final }}</td>
                                            <td>{{ elm.valor }}</td>
                                            <td>{{ elm.nom_aplica }}</td>
                                            <td>{{ elm.nom_status }}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div class="btn-group">
                        <button class="btn-insert" @click.prevent="CbtnIn">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-upload" viewBox="0 0 16 16">
                                <path
                                    d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5" />
                                <path
                                    d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708z" />
                                </svg>
                        </button>
                        <button class="btn-update" @click.prevent="CbtnUp">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-pencil-square" viewBox="0 0 16 16">
                                <path
                                    d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                                <path fill-rule="evenodd"
                                    d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z" />
                            </svg>
                        </button>
                        <button class="btn-delete" @click.prevent="CbtnDl">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-trash3" viewBox="0 0 16 16">
                                <path
                                    d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5" />
                            </svg>
                        </button>
                    </div>
                </div>
                <UpCargCaman v-if="btnUp" :cargo="cargo" :nombre="nombre" :tipo="tipo" :status="status" :btnUp="btnUp"
                    @updateProps="updatePropsValue" />
                <InCargCaman v-if="btnIn" :btnIn="btnIn" @insertProps="insertPropsValue" />
                 
            </section>
        </div>
    </body>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { Cargcaman, Cartarman } from '@/interface/interfaces';
import { stringifyQuery } from 'vue-router';
import { UrlGlobal } from '@/store/dominioGlobal';
import InCargCaman from './pInsert/InCargCaman.vue';
import UpCargCaman from './pUpdate/UpCargCaman.vue';

const dUrl = UrlGlobal()
const cargoRef = ref<string | null >(null)

//-----------------------------------------------------------------
const cargcaman = ref<Array<Cargcaman>>([]);
const getCargos = () => {
    axios.get(`${dUrl.urlGlobal}/api2/cargcaman`)
        .then(response => {
            cargcaman.value = response.data;

            //console.log(cargcaman.value[0].naturaleza)
        })
        .catch(error => {
            console.error('Error al Accesar los Cargos:', error);
        });
};
//----------------------------------------------------------------
const cartarman = ref<Array<Cartarman>>([])

const getVigencias = (id_tarifa: any, id_cargo: any, id_nombre: any, id_tipo: any, id_status: any) => {
    cargoRef.value = id_cargo
    axios.get(`${dUrl.urlGlobal}/api2/cargcaman/cartarman?id_tarifa=${id_tarifa}&id_cargo=${id_cargo}`)
        .then(response => {
            cartarman.value = response.data;

        if (clickUp.value) {
            console.log(id_cargo)
            console.log(id_nombre)
            FunClick(id_cargo, id_nombre, id_tipo, id_status)
        }
        })
        .catch(error => {
            console.error('Error al cargar los Cargos:', error);
        });
};
//funcion de los botones y las extenciones de Insert,delete,update----------------
let cargo : any
let nombre : any
let tipo : any
let status: any

let btnUp = ref(false);//variable para mostrar modal de update
let clickUp = ref(false)//variable para activar el click de Up
let btnIn = ref(false);//variable modal insert
let btnDl = ref(false);//variable para mostrar modal del delete
let clickDl = ref(false);//variable para activar el click del delete

let btnTaUp = ref(false);
let clickTaUp = ref(false);
let btnTaIn = ref(false);
let btnTaDl = ref(false);
let clickTaDl = ref(false);

//funciones q activan el click y en el caso del insert muestran el modal
const CbtnUp = () => {
  clickUp.value = !clickUp.value
  clickDl.value = false
}
const CbtnIn = () => {
  btnIn.value = !btnIn.value
  clickUp.value = false
  clickDl.value = false
}

const CbtnDl = () => {
  clickDl.value = !clickDl.value
  clickUp.value = false
}

const CbtnTaIn = () => {
  btnTaIn.value = !btnTaIn.value
  clickTaUp.value = false
  clickTaDl.value = false
}
const CbtnTaUp = () => {
  clickTaUp.value = !clickTaUp.value
  clickTaDl.value = false
}

const CbtnTaDl = () => {
  clickTaDl.value = !clickTaDl.value
  clickTaUp.value = false
}
//funcion principal para el funcionamiento de el update y delete cuando uno de los 2 este activado
const FunClick = (al: any, ar: any, an: any, st: any) => {
  let cargo = al;
  let nombre = ar;
  let tipo = an;
  let status = st;

  if (clickUp.value == true) {
    btnUp.value = !btnUp.value
    clickUp.value = !clickUp.value
  }
  if (clickDl.value == true) {
    btnDl.value = !btnDl.value
    clickDl.value = !clickDl.value
  }

  if (clickTaUp.value == true) {
    btnTaUp.value = !btnTaUp.value
    clickTaUp.value = !clickTaUp.value
  }

  if (clickTaDl.value == true) {
    btnTaDl.value = !btnTaDl.value
    clickTaDl.value = !clickTaDl.value
  }
}
//funciones de emits para actualizar las variables y cierre los modales activos sea de update o insert
function 
updatePropsValue(newValue: boolean, cargo: any) {
  btnUp.value = newValue
  cargo.value = String
   
  getCargos() 
  getVigencias('02', cargo.value, '', '', '')
}

function insertPropsValue(newValue: boolean) {
  btnIn.value = newValue
  getCargos();   
  getVigencias('02', '', '', '', '')
}
//---- Tarifas
function updTaPropsValue(newValue: boolean, tarifa: any, fecha: any,cargo: any, status: any) {
  btnTaUp.value = newValue
  tarifa.value = tarifa
  fecha.value = fecha
  cargo.value = cargo
  status.value = status

  getCargos()  
  getVigencias('', '', '', '', '')
}

function insTaPropsValue(newValue: boolean, tarifa: any, fecha: any, cargo: any ) {
  btnTaIn.value = newValue
  tarifa.value = tarifa
  fecha.value = fecha
  cargo.value = cargo

  getCargos();   
  getVigencias('', '', '', '', '')
}
//----------------------------------------------------------------

onMounted(() => {
    getCargos();
    getVigencias("02", "01", '', '', '')
});
</script>

<style scoped>
body {
    height: 100%;
    width: 100%;
    background: transparent;
    backdrop-filter: blur(10px);
}

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
    font-family: Trebuchet MS;
    color: white;
    background: linear-gradient(to right, #ccd0cf, #9ba8ab, #4a5c6a);
    overflow: hidden;
    @media screen and (max-width:600px){
        overflow: scroll;
    }
}

.layout {
    position: absolute;
    width: 95%;
    height: 95%;

    display: grid;
    grid:
        "header" auto "container" 1fr / 1fr;
    gap: 8px;
}

.header {
    grid-area: header;
}

.container {
    grid-area: container;
}
.card{
    width: 85%;
    height: 150px;
    min-width:min-content;
    box-sizing: border-box;
}
</style>