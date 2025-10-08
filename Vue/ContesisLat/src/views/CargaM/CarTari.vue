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
              style="background-color: transparent; border: none; outline: none; color: white;" autocomplete="off"
              v-model="search">
          </div>
        </div>
        <div class="container">
          <div class="row">
            <div class="col d-flex flex-column justify-content-center align-items-center">
              <h3><strong>Tarifas de Refrigeración</strong></h3>
              <div class="card overflow-scroll">
                <table class="table table-hover table-sm">
                  <thead>
                    <tr>
                      <th>Fecha Inicio</th>
                      <th>Fecha Final</th>
                      <th>Entrada</th>
                      <th>U/Medida</th>
                      <th>Peso/Base</th>
                      <th>Costo/Diario</th>
                      <th>Mín. Diario</th>
                      <th>Full Pallet</th>
                      <th>Estado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="elm in filteredCarga" :key="elm.fecha_inicio" 
                      @click="FunClick(elm.fecha_inicio, elm.fecha_final, elm.entrada, elm.medida,
                                elm.peso_base, elm.costo_diario, elm.minimo_diario, 
                                elm.full_pallet, elm.status)">
                      <td>{{ elm.fecha_inicio }}</td>
                      <td>{{ elm.fecha_final }}</td>
                      <td>{{ elm.entrada }}</td>
                      <td>{{ elm.medida }}</td>
                      <td>{{ elm.peso_base }}</td>
                      <td>{{ elm.costo_diario }}</td>
                      <td>{{ elm.minimo_diario }}</td>
                      <td>{{ elm.full_pallet }}</td>
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
        </div>
        <UpCarTari v-if="btnUp" :fecha_inicio="fecha_inicio" :entrada="entrada" :medida="medida" :peso_base="peso_base" 
            :costo_diario="costo_diario" :minimo_diario="minimo_diario" :full_pallet="full_pallet" :status="status" :btnUp="btnUp"
          @updateProps="updatePropsValue" />
        <InCarTari v-if="btnIn" :btnIn="btnIn" @insertProps="insertPropsValue" />
      </section>
    </div>
  </body>
</template>

<script lang="ts" setup>
import { ref, onMounted,computed } from 'vue';
import axios from 'axios';
import { Cartari } from '@/interface/interfaces'
import { UrlGlobal } from '@/store/dominioGlobal';
import UpCarTari from './pUpdate/UpCarTari.vue';
import InCarTari from './pInsert/InCarTari.vue';

const dUrl = UrlGlobal()

const tarifa = ref<Array<Cartari>>([]);
const search = ref('')

const getTarifa = (id_tarifa='03') => {
  axios.get(`${dUrl.urlGlobal}/api2/cartari?id_tarifa=${id_tarifa}`)
    .then(response => {
      tarifa.value = response.data;

      console.log(tarifa.value)
    }
  
  )
    .catch(error => {
      console.error('Error Buscando Tarifas:', error);
    });
};

const filteredCarga = computed(() => {
  if (search.value === '') {
    // Si no hay nada en la búsqueda, retornar todos los registros
    return tarifa.value;
  } else {
    // Convertir el término de búsqueda a minúsculas para hacer la búsqueda insensible a mayúsculas
    const searchTerm = search.value.toLowerCase();

    // Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos
    return tarifa.value.filter(elm => {
      return (
        elm.id?.toLowerCase().includes(searchTerm) ||
        elm.fecha_inicio?.toLowerCase().includes(searchTerm) ||
        elm.fecha_final?.toLowerCase().includes(searchTerm) ||
        elm.entrada?.toLowerCase().includes(searchTerm) ||
        elm.medida?.toLowerCase().includes(searchTerm) ||
        elm.costo_diario?.toLowerCase().includes(searchTerm)||
        elm.minimo_diario?.toLowerCase().includes(searchTerm) ||
        elm.full_pallet?.toLowerCase().includes(searchTerm) ||
        elm.nom_status?.toLowerCase().includes(searchTerm) 
      );
    });
  }
});

//funcion de los botones y las extenciones de Insert,delete,update----------------
let fecha_inicio: any
let fecha_final: any
let entrada: any
let medida: any
let peso_base: any
let costo_diario: any
let minimo_diario: any
let full_pallet: any 
let status: any
let id_ref: any
let btnUp = ref(false);//variable para mostrar modal de update
let clickUp = ref(false)//variable para activar el click de Up
let btnIn = ref(false);//variable modal insert
let btnDl = ref(false);//variable para mostrar modal del delete
let clickDl = ref(false);//variable para activar el click del delete

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
//funcion principal para el funcionamiento de el update y delete cuando uno de los 2 este activado
const FunClick = (fi: any, ff: any, en: any, med: any, pb: any, cd: any, md: any, fp: any, st: any ) => {
  fecha_inicio = fi;
  fecha_final = ff;
  entrada = en;
  medida = med;
  peso_base = pb;
  costo_diario = cd;
  minimo_diario = md;
  full_pallet = fp;
  status = st;

  if (clickUp.value == true) {
    btnUp.value = !btnUp.value
    clickUp.value = !clickUp.value
  }
  if (clickDl.value == true) {
    btnDl.value = !btnDl.value
    clickDl.value = !clickDl.value
  }
}

//funciones de emits para actualizar las variables y cierre los modales activos sea de update o insert
function updatePropsValue(newValue: boolean) {
  btnUp.value = newValue
  getTarifa("03")
}
function insertPropsValue(newValue: boolean) {
  btnIn.value = newValue
  getTarifa("03");
}

onMounted(() => {
  getTarifa("03");
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
  height: 250px;
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
</style>