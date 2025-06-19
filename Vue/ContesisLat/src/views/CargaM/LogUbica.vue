<template>

    <body>
        <div class="Card">
            <section class="layout">
                <div class="header">
                    <div class="btn-search">
                        <span><svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" fill="currentColor"
                                class="bi bi-search" viewBox="0 0 16 16">
                                <path
                                    d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0" />
                            </svg></span>
                        <input type="search" id="search" placeholder="Buscar"
                            style="background-color: transparent; border: none; outline: none; color: white;"
                            autocomplete="off" v-model="search">
                        <select
                            style="background-color: transparent; border: none; outline: none; color: black;"
                            v-model="options">
                            <option disabled value="">Select</option>
                            <option>Fecha</option>
                            <option>Operador</option>
                            <option>AirWayBill</option>
                        </select>
                    </div>
                </div>
                <div class="container">
                    <div class="row">
                        <div class="col d-flex flex-column justify-content-center align-items-center">
                            <h3><strong>Areas por Almacenes</strong></h3>
                            <div class="card overflow-scroll">
                                <table class="table table-hover  table-sm">
                                    <thead>
                                        <tr>
                                            <th>Almacen</th>
                                            <th>Nombre</th>
                                            <th>Area</th>
                                            <th>Descripcion</th>
                                            <th>Estado</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="elm in filteredCarga1" :key="elm.area"
                                            @click="getLoganaquel(elm.almacen, elm.area, elm.descripcion, elm.status)">
                                            <td>{{ elm.almacen }}</td>
                                            <td>{{ elm.nom_almacen }}</td>
                                            <td>{{ elm.area }}</td>
                                            <td>{{ elm.descripcion }}</td>
                                            <td>{{ elm.nom_status }}</td>
                                        </tr>
                                    </tbody>
                                </table>
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
                    </div>
                    <div class="row">
                        <div class="col d-flex flex-column justify-content-center align-items-center">
                            <h3><strong>Anaqueles</strong></h3>
                            <div class="card overflow-scroll">
                                <table class="table table-hover  table-sm">
                                    <thead>
                                        <tr>
                                            <th>Anaquel</th>
                                            <th>Cara</th>
                                            <th>Estado</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="elm in filteredCarga2" :key="elm.area"
                                            @click="getLogubica(elm.cara, elm.anaquel, elm.area, elm.almacen )">
                                            <td>{{ elm.anaquel }}</td>
                                            <td>{{ elm.cara }}</td>
                                            <td>{{ elm.nom_status}}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="btn-group">
                                <button class="btn-insert" @click.prevent="CbtnLaIn">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                        class="bi bi-upload" viewBox="0 0 16 16">
                                        <path
                                            d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5" />
                                        <path
                                            d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708z" />
                                    </svg>
                                </button>
                                <button class="btn-update" @click.prevent="CbtnLaUp">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                        class="bi bi-pencil-square" viewBox="0 0 16 16">
                                        <path
                                            d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                                        <path fill-rule="evenodd"
                                            d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z" />
                                    </svg>
                                </button>
                                <button class="btn-delete" @click.prevent="CbtnLaDl">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                        class="bi bi-trash3" viewBox="0 0 16 16">
                                        <path
                                            d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5" />
                                    </svg>
                                </button>
                            </div>

                        </div>
                    </div>
                    <div class="row">
                        <div class="col d-flex flex-column justify-content-center align-items-center">
                            <h3><strong>Ubicaciones</strong></h3>
                            <div class="card overflow-scroll">
                                <table class="table table-hover  table-sm">
                                    <thead>
                                        <tr>
                                            <th>Fila</th>
                                            <th>Columna</th>
                                            <th>Ubicacion</th>
                                            <th>Estado</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="elm in filteredCarga3" :key="elm.ubicacion" 
                                            @click="FunClick(elm.almacen, elm.area, elm.status, elm.anaquel, elm.cara, elm.fila, elm.columna, elm.ubicacion, null)">
                                            <td>{{ elm.fila }}</td>
                                            <td>{{ elm.columna }}</td>
                                            <td>{{ elm.ubicacion }}</td>
                                            <td>{{ elm.nom_status }}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="btn-group">
                                <button class="btn-insert" @click.prevent="CbtnLuIn">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                        class="bi bi-upload" viewBox="0 0 16 16">
                                        <path
                                            d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5" />
                                        <path
                                            d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708z" />
                                    </svg>
                                </button>
                                <button class="btn-update" @click.prevent="CbtnLuUp">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                        class="bi bi-pencil-square" viewBox="0 0 16 16">
                                        <path
                                            d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                                        <path fill-rule="evenodd"
                                            d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z" />
                                    </svg>
                                </button>
                                <button class="btn-delete" @click.prevent="CbtnLuDl">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                        class="bi bi-trash3" viewBox="0 0 16 16">
                                        <path
                                            d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <UpLogArea v-if="btnUp" :almacen="almacen" :area="area" :descripcion="descripcion" :status="status" :btnUp="btnUp"
                    @updProps="updLogareaPropsValue" />
                <InLogArea v-if="btnIn" :btnIn="btnIn" @insertProps="insLogareaPropsValue" />
                <DlLogArea v-if="btnDl" :btnDl="btnDl" :almacen="almacen" :area="area" @deleteProps="delLogareaPropsValue" />
                <UpLogAnaquel v-if="btnLaUp" :almacen="almacen" :area="area" :status="status" :anaquel="anaquel" :cara="cara" :btnLaUp="btnLaUp"
                    @updLaProps="updLoganaquelPropsValue" />
                <InLogAnaquel v-if="btnLaIn" :btnLaIn="btnLaIn" :almacen="almacen" :area="area" :status="status" @insLaProps="insLoganaquelPropsValue" />
                <DlLogAnaquel v-if="btnLaDl" :btnLaDl="btnLaDl" :almacen="almacen" :area="area" :anaquel="anaquel" :cara="cara" @delLaProps="delLoganaquelPropsValue" />
                <UpLogUbica v-if="btnLuUp" :status="status" :anaquel="anaquel" :cara="cara" :fila="fila" :columna="columna" :ubicacion="ubicacion" :btnLuUp="btnLuUp"
                    @updLuProps="updLogubicaPropsValue" />
                <InLogUbica v-if="btnLuIn" :btnLuIn="btnLuIn" :almacen="almacen" :area="area" :anaquel="anaquel" :cara="cara" @inLuProps="insLogubicaPropsValue" />
                <DlLogUbica v-if="btnLuDl" :btnLuDl="btnLuDl" :almacen="almacen" :area="area" :anaquel="anaquel" :cara="cara" :fila="fila" :columna="columna" @delLuProps="delLogubicaPropsValue" />
            </section>
        </div>
    </body>
</template>

<script lang="ts" setup>
import { ref, onMounted, computed,Ref } from 'vue';
import axios from 'axios';
import { Logarea, Loganaquel, Logubica} from '@/interface/interfaces';
import UpLogArea from './pUpdate/UpLogArea.vue';
import InLogArea from './pInsert/InLogArea.vue';
import DlLogArea from './pDelete/DlLogArea.vue';
import InLogAnaquel from './pInsert/InLogAnaquel.vue';
import UpLogAnaquel from './pUpdate/UpLogAnaquel.vue';
import DlLogAnaquel from './pDelete/DlLogAnaquel.vue';
import InLogUbica from './pInsert/InLogUbica.vue';
import UpLogUbica from './pUpdate/UpLogUbica.vue';
import DlLogUbica from './pDelete/DlLogUbica.vue';

import { UrlGlobal } from '@/store/dominioGlobal';
import { stringifyQuery } from 'vue-router';

const dUrl = UrlGlobal()
const search = ref('')
const options = ref('')
const varP = ref(0)
//const cara = ref('')
const nom_status = ref('')
let carau = String
//const fila = ref('')
//const columna = ref('')
const ubicacion = ref('')

//-----------------------------------------------------------------
const logarea = ref<Array<Logarea>>([]);

const getLogarea = () => { 
        axios.get(dUrl.urlGlobal +'/api2/logarea/')
            .then(response => {
                logarea.value = response.data;
        
            let almacen = response.data.almacen
            let area = response.data.area

            })
            .catch(error => {
                console.error('Error fetching cargos:', error);
            });
};
//----------------------------------------------------------------
const loganaquelz = ref<Array<Loganaquel>>([])
const getLoganaquel = (id_almacen: any, id_area: any, id_descripcion: any, id_status: any) => {
     
        axios.get(`${dUrl.urlGlobal}/api2/logarea/loganaquel?id_area=${id_area}&id_almacen=${id_almacen}`)
            .then(response => { console.log(response.data)
                loganaquelz.value = response.data; 

                almacen = id_almacen
                area = id_area
                descripcion = id_descripcion
                status = id_status

                if (clickUp.value == true || clickDl.value == true) {
                    FunClick(almacen, area, status, null, null, null, null, null, descripcion)

                }
                
            })
            .catch(error => {
                console.error('Error fetching loganaquel:', error);
        });
    }
//};
//----------------------------------------------------------------
const logubica = ref<Array<Logubica>>([])
const getLogubica = (id_cara: any, id_anaquel: any, id_area: any, id_almacen: any) => {
    axios.get(`${dUrl.urlGlobal}/api2/loganaquel/logubica?id_cara=${id_cara}&id_anaquel=${id_anaquel}&id_area=${id_area}&id_almacen=${id_almacen}`)
        .then(response => {
            logubica.value = response.data;

            cara = id_cara
            anaquel = id_anaquel
            area = id_area
            //status = id_status
            almacen = id_almacen
            //fila = id_fila
            //columna.value = id_columna

            if (clickLaUp.value == true || clickLaDl.value == true) {
                    FunClick(almacen, area, status, anaquel, cara, null, null, null, null)

                }
        })
        .catch(error => {
            console.error('Error fetching logubica:', error);
        });
};
//-----------------------------------------------------------------
// Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos segun la tabla------------------------------------------------
const filteredCarga1 = computed(() => {
    if (search.value === '') {
        // Si no hay nada en la búsqueda, retornar todos los registros
        return logarea.value;
    } else if (options.value == 'Area') {
        // Convertir el término de búsqueda a minúsculas para hacer la búsqueda insensible a mayúsculas
        const searchTerm = search.value.toLowerCase();
        // Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos
        return logarea.value.filter(elm => {
            return (
                elm.almacen?.toLowerCase().includes(searchTerm) ||
                elm.nom_almacen?.toLowerCase().includes(searchTerm) ||
                elm.area?.toLowerCase().includes(searchTerm) ||
                elm.descripcion?.toLowerCase().includes(searchTerm) ||
                elm.nom_status?.toLowerCase().includes(searchTerm)
            );
        });
    }else{
        return logarea.value
    }
});
//----------------------------------------------------------------
const filteredCarga2 = computed(() => {
    if (search.value === '') {
        return loganaquelz.value;

    } else if (options.value == 'Anaqueles') {
        const searchTerm = search.value.toLowerCase();

        return loganaquelz.value.filter(elm => {
            return (
                elm.anaquel?.toLowerCase().includes(searchTerm) ||
                elm.cara?.toLowerCase().includes(searchTerm) ||
                elm.nom_status?.toLowerCase().includes(searchTerm) 
            );
        });
    }else{
        return loganaquelz.value
    }
});

//----------------------------------------------------------------
const filteredCarga3 = computed(() => {
    if (search.value === '') {
        return logubica.value;
    } else if (options.value == 'Ubicaciones') {
        const searchTerm = search.value.toLowerCase();
        return logubica.value.filter(elm => {
            return (
                elm.fila?.toLowerCase().includes(searchTerm) ||
                elm.columna?.toLowerCase().includes(searchTerm) ||
                elm.ubicacion?.toLowerCase().includes(searchTerm) ||
                elm.nom_status?.toLowerCase().includes(searchTerm)
            );
        });
    }else{
        return logubica.value
    }
});


//funcion de los botones y las extenciones de Insert,delete,update----------------
let almacen : any
let descripcion : any
let area : any
let anaquel: any 
let cara: any
let fila: any
let columna: any
let status: any

let btnUp = ref(false);//variable para mostrar modal de update
let clickUp = ref(false)//variable para activar el click de Up
let btnIn = ref(false);//variable modal insert
let btnDl = ref(false);//variable para mostrar modal del delete
let clickDl = ref(false);//variable para activar el click del delete

let btnLaUp = ref(false);
let clickLaUp = ref(false);
let btnLaIn = ref(false);
let btnLaDl = ref(false);
let clickLaDl = ref(false);

let btnLuUp = ref(false);
let clickLuUp = ref(false);
let btnLuIn = ref(false);
let btnLuDl = ref(false);
let clickLuDl = ref(false);


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

const CbtnLaIn = () => {
  btnLaIn.value = !btnLaIn.value
  clickLaUp.value = false
  clickLaDl.value = false
}
const CbtnLaUp = () => {
  clickLaUp.value = !clickLaUp.value
  clickLaDl.value = false
}

const CbtnLaDl = () => {
  clickLaDl.value = !clickLaDl.value
  clickLaUp.value = false
}

const CbtnLuUp = () => {
  clickLuUp.value = !clickLuUp.value
  clickLuDl.value = false
}
const CbtnLuIn = () => {
  btnLuIn.value = !btnLuIn.value
  clickLuUp.value = false
  clickLuDl.value = false
}

const CbtnLuDl = () => {
  clickLuDl.value = !clickLuDl.value
  clickLuUp.value = false
}
//funcion principal para el funcionamiento de el update y delete cuando uno de los 2 este activado
const FunClick = (al: any, ar: any, st: any, an: any, ca: any, fi: any, co: any, de: any, ub: any) => {
  let almacen = al;
  let area = ar;
  let status = st;
  let anaquel = an;
  let cara = ca;
  let fila = fi;
  let columna = co;
  let descripcion = de;
  let ubicacion = ub;

  if (clickUp.value == true) {
    btnUp.value = !btnUp.value
    clickUp.value = !clickUp.value
  }
  if (clickDl.value == true) {
    btnDl.value = !btnDl.value
    clickDl.value = !clickDl.value
  }

  if (clickLaUp.value == true) {
    btnLaUp.value = !btnLaUp.value
    clickLaUp.value = !clickLaUp.value
  }

  if (clickLaDl.value == true) {
    btnLaDl.value = !btnLaDl.value
    clickLaDl.value = !clickLaDl.value
  }

  if (clickLuUp.value == true) {
    btnLuUp.value = !btnLuUp.value
    clickLuUp.value = !clickLuUp.value
  }

  if (clickLuDl.value == true) {
    btnLuDl.value = !btnLuDl.value
    clickLuDl.value = !clickLuDl.value
  }
}

//funciones de emits para actualizar las variables y cierre los modales activos sea de update o insert
function updLogareaPropsValue(newValue: boolean) {
  btnUp.value = newValue
  //almacen.value = almacen
  //area.value = area
  //descripcion.value = descripcion
  //status.value = status

  getLogarea()  
}

//function insertPropsValue(newValue: boolean, var1: number) {
//  btnIn.value = newValue,
//  varP.value = var1
//  if (varP.value == 1){
//    getLogarea();
//  }
//  if (varP.value == 2){
//    getLogarea();
//  }
//}

function insLogareaPropsValue(newValue: boolean) {
  btnIn.value = newValue
  getLogarea();   
}

function delLogareaPropsValue(newValue: boolean, almacen: any, area: any) {
  btnDl.value = newValue
  almacen.value = String
  area.value = String

  getLogarea()
}
//---- Anaqueles
function updLoganaquelPropsValue(newValue: boolean, almacen: any, area: any, status: any, anaquel: any, cara: any) {
  btnLaUp.value = newValue
  almacen.value = almacen
  area.value = area
  anaquel.value = anaquel
  cara.value = cara
  status.value = status

  getLoganaquel(almacen, area, null, null)  
}

function insLoganaquelPropsValue(newValue: boolean, almacen: any, area: any ) {
  btnLaIn.value = newValue
  almacen.value = almacen
  area.value = area

  getLoganaquel(almacen, area, null, null);   
}

function delLoganaquelPropsValue(newValue: boolean, almacen: any, area: any, anaquel: any, cara: any) {
  btnLaDl.value = newValue
  almacen.value = almacen
  area.value = area
  anaquel.value = anaquel
  cara.value = cara

  getLoganaquel(almacen, area, null, null)
}
//--Ubicaciones    -----------------------------------------------------------------//almacen: any, area: any, anaquel: any, cara: any)
function updLogubicaPropsValue(newValue: boolean) {
  btnUp.value = newValue
  status.value = status
  fila.value = fila
  columna.value = columna
  //ubicacion.value = ubicacion
  //almacen.value = almacen
  //area.value = area
  //anaquel.value = anaquel
  //cara.value = cara

    getLogubica(almacen, area, anaquel, cara)  
}

function insLogubicaPropsValue(newValue: boolean, almacen: any, area: any, anaquel: any, carau: any ) {
  btnIn.value = newValue
  almacen.value = almacen
  area.value = area
  anaquel.value = anaquel
  cara.value = carau

    getLogubica(almacen, area, anaquel, cara);   
}

function delLogubicaPropsValue(newValue: boolean, almacen: any, area: any, anaquel: any, cara: any, fila: any, columna: any) {
  btnDl.value = newValue
  almacen.value = almacen
  area.value = area
  anaquel.value = anaquel
  cara.value = cara
  fila.value = fila
  columna.value = columna

    getLogubica(almacen, area, anaquel, cara)
}
//-----------------------------------------------------------------------------------------------------------------------

onMounted(() => {
    getLogarea();
    getLoganaquel("1", "1", null, null);
    getLogubica("1", "1", "1", "1")
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
    overflow: scroll;
    @media screen and (max-width: 600px){
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
    display: flex;
    justify-content: right;
    align-items: right;
    grid-area: header;
}

.container {
    grid-area: container;
}

.card {
    width: 85%;
    height: 150px;
    min-width: min-content;
    box-sizing: border-box;
}

.btn-search {
    border: none;
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
    color: white;
    padding-left: 3px;
    justify-content: space-between;
    display: flex;
    gap: 4px;
    min-width: min-content;
}

.btn-search:focus {
    outline: none;
}

.btn-group {
  display: flex;
  justify-content: flex-end;
  gap: 20px;
  margin-top: 20px;
}

.btn-group button {
  border: none;
  border-radius: 20px;
}

.btn-delete:hover,
.btn-delete:focus {
  background: #d94b6a;
  color: white;
}

.btn-update:hover,
.btn-update:focus {
  background: #bcd34a;
  color: white;
}

.btn-insert:hover,
.btn-insert:focus {
  background: #5d74b7;
  color: white;
}
</style>