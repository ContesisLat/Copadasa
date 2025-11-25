<template>
  <body>
    <div class="Card">
      <section class="layout">
          <div class="container">
              <div class="row" style="gap: 5px;">
                <div class="col d-flex flex-column justify-content-center align-item-center" >
                  <h3><strong>Manifiestos</strong></h3>
                  <div class="card overflow-scroll">
                      <table class="table table-hover  table-sm">
                          <thead>
                              <tr>
                                  <th>Fecha</th>
                                  <th>Operador</th>
                                  <th>No. Vuelo</th>
                                  <th>Pto. Despacho</th>
                                  <th>Pto. Destino</th>
                                  <th>Aeronave</th>
                                  <th>Matrícula</th>
                                  <th>Estado</th> 
                              </tr>
                          </thead>
                            <tbody>
                              <tr v-for="elm in filteredCarga1" :key="elm.numero_vuelo"
                                  @click="getCardmani(elm.numero_vuelo, elm.operador, elm.fecha, elm.id, elm.nom_operador)"
                                  :class="{ 'table-primary': elm.id === id_ref }">
                                  <td>{{ elm.fecha }}</td>
                                  <td>{{ elm.nom_operador }}</td>
                                  <td>{{ elm.numero_vuelo }}</td>
                                  <td>{{ elm.nom_pto_despacho }}</td>
                                  <td>{{ elm.nom_pto_destino }}</td>
                                  <td>{{ elm.nom_aeronave }}</td>
                                  <td>{{ elm.matricula }}</td>
                                  <td>{{ elm.nom_status}}</td>
                              </tr>
                            </tbody>
                      </table>  
                  </div>
                  <h3><strong>Air Way Bill por Manifiestos</strong></h3>
                  <div class="card overflow-scroll">
                      <table class="table table-hover  table-sm">
                          <thead>
                              <tr>
                                <th>Secuencia</th>
                                <th>No. Embarque</th>
                                <th>Naturaleza</th>
                                <th>Tot. Piezas</th>
                                <th>Peso Kg.</th>
                                <th>Destinatario</th>
                                <th>Ubicación</th>
                                <th>Estado</th>
                              </tr>
                          </thead>
                          <tbody>
                              <tr v-for="elm1 in filteredCarga2" :key="elm1.no_embarque"
                                 @click="getCardmaniId(elm1.id, elm1.status, elm1.no_embarque, elm1.numero_vuelo,
                                                       elm1.operador, elm1.fecha)" 
                                  :class="{ 'table-primary': elm1.id === de_ref }" >
                                <td>{{ elm1.secuencia }}</td>
                                <td>{{ elm1.no_embarque }}</td>
                                <td>{{ elm1.nom_naturaleza }}</td>
                                <td>{{ elm1.cant_items }}</td>
                                <td>{{ elm1.peso_kg }}</td>
                                <td>{{ elm1.destinatario }}</td>
                                <td>{{ elm1.ubicacion }}</td>
                                <td>{{ elm1.nom_status}}</td>
                              </tr>
                          </tbody>
                      </table>
                  </div>
                </div> 
                <div class="col div-buttom"
                      style=" background-color:rgba(255, 255, 255, 0.3);  backdrop-filter: blur(10px); border-radius: 10px; height: 300px;">
                      <div class="btn-group2">
                        <button type="button" class="btn btn-light" @click.prevent="Confirmar">Confirmar</button>
                        <button type="button" class="btn btn-light" @click="Complemento">Liquidación</button>
                        <button type="button" class="btn btn-light" @click="Calcular">Calcular</button>
                        <button type="button" class="btn btn-light" @click="Vercalculo" disabled>Ver Calculo</button>
                        <button type="button" class="btn btn-light" @click="Listar" :disabled="!canUseGroup2">Listar</button>
                        <!--button type="button" class="btn btn-light" @click="Anular" :disabled="!canUseGroup2">Anular</button-->
                      </div>
                </div>
              </div>
          </div>
          <UpConfirma v-if="btnUp" :fecha="fecha" :operador="operador" :numero_vuelo="numero_vuelo" 
              :no_embarque="no_embarque" :nom_operador="nom_operador" :btnUp="btnUp"
              @updateProps="updatePropsValue" />
          <UpComplemento v-if="btnCoUp" :fecha="fecha" :operador="operador" :numero_vuelo="numero_vuelo"
              :no_embarque="no_embarque" :btnCoUp="btnCoUp"
              @updateCoProps="updateCoPropsValue" />
          <UpVercalculo v-if="btnCaUp" :fecha="fecha" :operador="operador" :numero_vuelo="numero_vuelo" 
              :no_embarque="no_embarque" :btnCaUp="btnCaUp"
              @updateProps="updateCaPropsValue" />
      </section>
    </div>
  </body>
</template>

<script lang="ts" setup>
 
import { ref, onMounted, computed, Ref, defineProps, defineEmits } from 'vue';
import axios from 'axios';
import { useAlert } from '@/store/useAlert';
const {success, error, question,warning} = useAlert()
import { UrlGlobal } from '@/store/dominioGlobal';
const dUrl = UrlGlobal()
const search = ref('')
const options = ref('')
import { Carcmani, Cardmani } from '@/interface/interfaces';
import UpConfirma from './pUpdate/UpConfirma.vue';
import UpComplemento from './pUpdate/UpComplemento.vue';
import UpVercalculo from './UpVercalculo.vue';
import { flattenDiagnosticMessageText } from 'typescript';

const id_ref = ref<string | null>(null)
const de_ref = ref<string | null>(null)
const id_status = ref<string | null>(null)
//--------------------------------------------------------------------------------------------------------------
const carcmani = ref<Array<Carcmani>>([]);

const getCarcmani = () => { 
        axios.get(dUrl.urlGlobal +'/api2/carcmani/')
            .then(response => {
                carcmani.value = response.data;
        
            let fecha = response.data.fecha
            let operador = response.data.operador
            let numero_vuelo = response.data.numero_vuelo
            

            })
            .catch(error => {
                console.error('Error buscando control de Manifiestos:', error);
            });
};
const getCardmaniId = (id: any, sts: any, emb: any, novue: any, opera: any, fec: any) => {
  de_ref.value = id
  id_status.value = sts
  no_embarque = emb
  numero_vuelo = novue
  operador = opera
  fecha = fec 

  if(!de_ref.value) {
    return
  }

}
//----------------------------------------------------------------
const cardmani = ref<Array<Cardmani>>([])
const getCardmani = (id_numero_vuelo: any, id_operador: any, id_fecha: any, id: any, nom_opera: any) => {
        id_ref.value = id
        fecha = id_fecha
        operador = id_operador
        numero_vuelo = id_numero_vuelo
        nom_operador = nom_opera
        de_ref.value = null

        axios.get(`${dUrl.urlGlobal}/api2/carcmani/cardmani?id_numero_vuelo=${id_numero_vuelo}&id_operador=${id_operador}&id_fecha=${id_fecha}`)
        //axios.get(final)    
            .then(response => { //console.log(response.data)
                cardmani.value = response.data;
                console.log(response.data)

                
            })
            .catch(error => {
                console.error('Error buscando detalles de manifiesto:', error);
        });
    }
//};
//funcion de los botones y las extenciones de Insert,delete,update----------------
let fecha: any
let operador: any
let numero_vuelo: any
let no_embarque: any
let nom_operador: any

let btnUp = ref(false);//variable para mostrar modal de update
let clickUp = ref(false)//variable para activar el click de Up
let btnCoUp = ref(false)
let clickCoUp = ref(false)
let btnCaUp = ref(false)
let clickCaUp = ref(false)

    

//funciones q activan el click y en el caso del insert muestran el modal
const CbtnUp = () => {
  clickUp.value = !clickUp.value
   
}
function updatePropsValue(newValue: boolean) {
  btnUp.value = newValue
  getCarcmani()
  getCardmani(numero_vuelo, operador, fecha, null,null)
}

function updateCoPropsValue(newValue: boolean) {
  btnCoUp.value = newValue

  getCarcmani()
  getCardmani(numero_vuelo, operador, fecha, null, null)
}

function updateCaPropsValue(newValue: boolean) {
  btnCaUp.value = newValue

  getCarcmani()
  getCardmani(numero_vuelo, operador, fecha, null, null)
}
//--- Fun//funcion principal para el funcionamiento de el update y delete cuando uno de los 2 este activado
const FunClick = (n: any, nm: any, st: any) => {
  fecha = n;
  operador = nm;
  numero_vuelo = st;

  if (clickUp.value == true) {
    btnUp.value = !btnUp.value
    clickUp.value = !clickUp.value
  }
}
  //-- Funciones de Botones
const Calcular = async() => {
  let calcular = true
  if (!de_ref.value) {
    return
  }

  if (id_status.value =='K' || id_status.value =='C') {
    null
  } else {
    return
  }
    
  const result = await question(
    'Se generarán los calculos de la Guía',
    '¿Seguro desea continuar?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }

  axios.get(`${dUrl.urlGlobal}/api2/carcmani/calculo?id=${de_ref.value}`) 
    .then(response => {
      console.log("Generado")
      getCarcmani
      getCardmani(numero_vuelo, operador, fecha, null, null)
    })
    .catch(error => {
      console.log('Error calculando:', error)
    })
}

const Vercalculo = () => {
  if (!de_ref.value) {
    return
  }

  if (id_status.value !='C') {
    return
  }

  clickCaUp.value = !clickCaUp.value

  if (clickCaUp.value == true) {
      btnCaUp.value = !btnCaUp.value
      clickCaUp.value = !clickCaUp.value
  }
}

const Confirmar = () => {
  if (!de_ref.value) {
    return
  }

  if (id_status.value != 'R' && id_status.value !='L') {
    return
  }

  clickUp.value = !clickUp.value

  if (clickUp.value == true) {
    btnUp.value = !btnUp.value
    clickUp.value = !clickUp.value
  } 
}

const Complemento = () => {
   if (!de_ref.value) {
    return
  }
  //'L' es Confirmado
  if (id_status.value == 'C' || id_status.value =='R' || id_status.value =='D') {
    return
  }

  clickCoUp.value = !clickCoUp.value

  if (clickCoUp.value == true) {
    btnCoUp.value = !btnCoUp.value
    clickCoUp.value = !clickCoUp.value
  }
}

const Listar = () => {
  let calcular = false
}

const Anular = () => {
  let calcular = false
}

//-----------------------------------------------------------------
// Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos segun la tabla------------------------------------------------
const filteredCarga1 = computed(() => {
    if (search.value === '') {
        // Si no hay nada en la búsqueda, retornar todos los registros
        return carcmani.value;
    } else if (options.value == 'fecha') {
        // Convertir el término de búsqueda a minúsculas para hacer la búsqueda insensible a mayúsculas
        const searchTerm = search.value.toLowerCase();
        // Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos
        return carcmani.value.filter(elm => {
            return (
                elm.fecha?.toLowerCase().includes(searchTerm) ||
                elm.nom_operador?.toLowerCase().includes(searchTerm) ||
                elm.numero_vuelo?.toLowerCase().includes(searchTerm) ||
                elm.nom_pto_despacho?.toLowerCase().includes(searchTerm) ||
                elm.nom_pto_destino?.toLowerCase().includes(searchTerm) ||
                //elm.tot_piezas?.toLowerCase().includes(searchTerm) ||
                //elm.peso_kg?.toLowerCase().includes(searchTerm) ||
                elm.nom_aeronave?.toLowerCase().includes(searchTerm) ||
                elm.matricula?.toLowerCase().includes(searchTerm) ||
                elm.nom_status?.toLowerCase().includes(searchTerm)
            );
        });
    }else{
        return carcmani.value
    }
});
//-----------------------------------------------------------------
const filteredCarga2 = computed(() => {
    if (search.value === '') {
        return cardmani.value;

    } else if (options.value == 'Cardmani') {
        const searchTerm = search.value.toLowerCase();

        console.log(de_ref.value)

        return cardmani.value.filter(elm1 => {
            return (
                elm1.fecha?.toLocaleLowerCase().includes(searchTerm) ||
                elm1.operador?.toLocaleLowerCase().includes(searchTerm) ||
                elm1.numero_vuelo?.toLocaleLowerCase().includes(searchTerm) ||
                elm1.no_embarque?.toLowerCase().includes(searchTerm)
                
            );
        });
    }else{
        return cardmani.value
    }
});

//const FunClick = (fe: any, op: any, nv: any) => {
//  let fecha = fe;
//  let operador = op;
//  let numero_vuelo = nv;
   
//----------------------------------------------------------------
// Estado del formulario y la data
//const formData = ref({
//  base_datos: '',
//  tipo_base_datos: '',
//  servidor_bdatos: '',
//  hostname: '',
//  ip_address: '',
//  servicio: '',
//  puerto: '',
//  protocolo: ''
//});

// Variables de control
const dataList = ref<any[]>([]); // Lista de datos de la API
const currentIndex = ref(0);
const isEditing = ref(false);
const isSearching = ref(false);
const isInserting = ref(false);
const isDeleting = ref(false);
const canNavigate = ref(false);
const onlyRead = ref(true);
const ButtonText = ref('Conf')
const ButtonText2 = ref('Complto')
const ButtonText3 = ref('Calcula')
const ButtonText4 = ref('Anular')

// Deshabilita los botones de btn-group2 si no está en modo búsqueda o insercion
const canUseGroup2 = computed(() => isSearching.value || isInserting.value || isEditing.value || isDeleting.value);

//boton principal que controla el submit

//------------------------------------------------------------------------------------------------------------------
onMounted(() => {
    getCarcmani();
    console.log(carcmani)
    getCardmani(null, "1", "1",null, null);
  
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

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
  font-family: 'Poppins', sans-serif;
  color: white;
  background: linear-gradient(to right, #ccd0cf, #9ba8ab, #4a5c6a);
  overflow: scroll;

  @media screen and (max-width: 600px) {
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
  gap: 50px;
}

.header {
  display: flex;
  justify-content: left;
  align-items: left;
  grid-area: header;
}

.container {
  grid-area: container;
}
.card {
    width: 100%;
    height: 200px;
    min-width: min-content;
    box-sizing: border-box;
}

.btn-group {
  display: flex;
  justify-content: flex-end;
  gap: 20px;
  margin-top: 20px;
  padding: 5px;
  background-color: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
  border: none;
  border-radius: 10px;
}

.btn-group button {
  border: none;
  border-radius: 20px;
  background-color: transparent;
  transition: transform 0.2s ease;
}

.btn-group button:active {
  transform: scale(0.95);
}

.btn-group button:hover {
  background: #001982;
  color: white;
}

.btn-group2 {
  display: flex;
  height: 250px;
  justify-content: center;
  flex-direction: column;
  gap: 20px;
  margin-top: 20px;
  padding: 5px;
  border: none;
  border-radius: 10px;
}

.btn-group2 button {
  transition: transform 0.2s ease;
  overflow: hidden;
}

.btn-group2 button:active {
  transform: scale(0.95);
}

.div-buttom{
  max-width: 200px;
  overflow: hidden;
}
</style>