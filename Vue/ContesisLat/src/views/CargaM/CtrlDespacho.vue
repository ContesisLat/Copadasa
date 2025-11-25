<template>
  <body>
    <div class="Card">
      <section class="layout">
          <div class="container">
              <div class="row" style="gap: 5px;">
                <div class="col d-flex flex-column justify-content-center align-item-center" >
                  <h3><strong>Control de Despachos</strong></h3>
                  <div class="card overflow-scroll w-100">
                      <table class="table table-hover  table-sm">
                          <thead>
                              <tr>
                                  <th>Fecha</th>
                                  <th>Operador</th>
                                  <th>No. Vuelo</th>
                                  <th>No. Embarque</th>
                                  <th>Destinatario</th>
                                  <th>Piezas</th>
                                  <th>Peso</th>
                                  <th>Estado</th> 
                              </tr>
                          </thead>
                            <tbody>
                              <tr v-for="elm in filteredCarga1" :key="elm.numero_vuelo"
                                  @click="getCardeent(elm.fecha, elm.fecha_manifiesto, elm.operador, elm.numero_vuelo, elm.no_embarque, elm.id)" 
                                  :class="{ 'table-primary': elm.no_embarque === id_ref }">
                                  <td>{{ elm.fecha_manifiesto }}</td>
                                  <td>{{ elm.nom_operador }}</td>
                                  <td>{{ elm.numero_vuelo }}</td>
                                  <td>{{ elm.no_embarque }}</td>
                                  <td>{{ elm.destinatario }}</td>
                                  <td>{{ elm.piezas_entrega }}</td>
                                  <td>{{ elm.peso }}</td>
                                  <td>{{ elm.nom_status}}</td>
                              </tr>
                            </tbody>
                      </table>  
                  </div>
                  <h3><strong>Cargos Generados</strong></h3>
                  <div class="card overflow-scroll w-100" style="height: 150px;">
                      <table class="table table-hover  table-sm">
                          <thead>
                              <tr>
                                <th>Cargo</th>
                                <th>Descripción</th>
                                <th>Monto</th>
                                <th>Estado</th>
                              </tr>
                          </thead>
                          <tbody>
                              <tr v-for="elm1 in cardeent" :key="elm1.tarifa"> 
                                 <!--@click="true" :class="{ 'table-primary': elm1.id === de_ref }" -->
                                <td>{{ elm1.tarifa }}</td>
                                <td>{{ elm1.nom_tarifa }}</td>
                                <td>{{ elm1.monto }}</td>
                                <td>{{ elm1.nom_status}}</td>
                              </tr>
                          </tbody>
                      </table>
                  </div>
                </div> 
                <div class="col div-buttom"
                      style=" background-color:rgba(255, 255, 255, 0.3);  backdrop-filter: blur(10px); border-radius: 10px; height: 300px;">
                      <div class="btn-group2">
                        <button type="button" class="btn btn-light" @click.prevent="CbtnDE">Datos Entrega</button>
                        <button type="button" class="btn btn-light" @click="Complemento" disabled>Despacho</button>
                        <button type="button" class="btn btn-light" @click="Listar" :disabled="!canUseGroup2">Imprimir</button>
                        <button type="button" class="btn btn-light" @click="Anular" :disabled="!canUseGroup2">Anular</button>
                      </div>
                </div>
              </div>
          </div>
          <UpConfirma v-if="btnUp" :fecha="fecha" :operador="operador" :numero_vuelo="numero_vuelo" :btnUp="btnUp"
              @updateProps="updatePropsValue" />
          <UpComplemento v-if="btnCoUp" :fecha="fecha" :operador="operador" :numero_vuelo="numero_vuelo" :btnCoUp="btnCoUp"
              @updateCoProps="updateCoPropsValue" />
              
      </section>
    </div> 
    <InDatosE v-if="btnDE" :BdatosE="btnDE" :numembarque="no_embarque" @DEpropsValue="DEPropsValue"/>
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
import { Carentre, Cardeent } from '@/interface/interfaces';
import UpConfirma from './pUpdate/UpConfirma.vue';
import UpComplemento from './pUpdate/UpComplemento.vue';
import InDatosE from './pInsert/InDatosE.vue';
import { flattenDiagnosticMessageText } from 'typescript';

const id_ref = ref<string | null>(null)
const de_ref = ref<string | null>(null)
//--------------------------------------------------------------------------------------------------------------
const carentre = ref<Array<Carentre>>([]);

const getCarentre = () => { 
        axios.get(dUrl.urlGlobal +'/api2/carentre/')
            .then(response => {
                carentre.value = response.data;
        
            //let almacen = response.data.almacen
            //let area = response.data.area

            })
            .catch(error => {
                console.error('Error buscando control de despachos:', error);
            });
};
//----------------------------------------------------------------
const cardeent = ref<Array<Cardeent>>([])
const getCardeent = (id_fecha: any, id_fecha_manifiesto: any, id_operador: any, id_numero_vuelo: any, id_no_embarque: any, id: any) => {
        id_ref.value = id_no_embarque
        fecha = id_fecha
        fecha_manifiesto = id_fecha_manifiesto
        operador = id_operador
        numero_vuelo = id_numero_vuelo
        no_embarque = id_no_embarque

        axios.get(`${dUrl.urlGlobal}/api2/carentre/cardeent?id_no_embarque=${no_embarque}&id_numero_vuelo=${numero_vuelo}&id_operador=${operador}
                  &id_fecha_manifiesto=${fecha_manifiesto}&id_fecha=${fecha}`)
        //axios.get(final)    
            .then(response => { //console.log(response.data)
                cardeent.value = response.data;
                console.log(response.data)

                
            })
            .catch((error: any) => {
                console.error('Error buscando detalles de despacho:', error);
        });
    }
//};
//funcion de los botones y las extenciones de Insert,delete,update----------------
let fecha: any
let fecha_manifiesto: any
let operador: any
let numero_vuelo: any
let no_embarque: any

let btnUp = ref(false);//variable para mostrar modal de update
let clickUp = ref(false)//variable para activar el click de Up
let btnCoUp = ref(false)
let clickCoUp = ref(false)

//funciones q activan el click y en el caso del insert muestran el modal
const CbtnUp = () => {
  clickUp.value = !clickUp.value
   
}
function updatePropsValue(newValue: boolean) {
  btnUp.value = newValue
  getCarentre()
  getCardeent("1", "1", "1", "1", "1", "1")
}

function updateCoPropsValue(newValue: boolean) {
  btnCoUp.value = newValue

  getCarentre()
  getCardeent("1", "1", "1", "1", "1", "1")
}

const btnDE = ref(false)
const CbtnDE= () => {
  btnDE.value = !btnDE.value
   
}
function DEPropsValue(newValue: boolean) {
  btnDE.value = newValue
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
  
  const result = await question(
    'Se generarán los calculos de la Guía',
    '¿Seguro desea continuar?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }

  axios.get(`${dUrl.urlGlobal}/api2/carcmani/calculo?id=${id_ref.value}`) 
    .then(response => {
      console.log("Generado")
      getCarentre
      getCardeent("1", "1", "1", "1", "1", "1")
    })
    .catch(error => {
      console.log('Error calculando:', error)
    })
}


const Complemento = () => {
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
        return carentre.value;
    } else if (options.value == 'fecha') {
        // Convertir el término de búsqueda a minúsculas para hacer la búsqueda insensible a mayúsculas
        const searchTerm = search.value.toLowerCase();
        // Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos
        return carentre.value.filter(elm => {
            return (
                elm.fecha?.toLowerCase().includes(searchTerm) ||
                elm.fecha_manifiesto?.toLocaleLowerCase().includes(searchTerm) ||
                elm.nom_operador?.toLowerCase().includes(searchTerm) ||
                elm.numero_vuelo?.toLowerCase().includes(searchTerm) ||
                elm.destinatario?.toLowerCase().includes(searchTerm) ||
                elm.piezas_entrega?.toLowerCase().includes(searchTerm) ||
                elm.monto?.toLowerCase().includes(searchTerm) ||
                elm.nom_status?.toLowerCase().includes(searchTerm)
            );
        });
    }else{
        return carentre.value
    }
});
//-----------------------------------------------------------------
const filteredCarga2 = computed(() => {
    if (search.value === '') {
        return cardeent.value;

    } else if (options.value == 'Cardeent') {
        const searchTerm = search.value.toLowerCase();

        return cardeent.value.filter(elm1 => {
            return (
                elm1.nom_tarifa?.toLowerCase().includes(searchTerm) ||
                elm1.monto?.toLowerCase().includes(searchTerm) ||
                elm1.nom_status?.toLowerCase().includes(searchTerm) 
            );
        });
    }else{
        return cardeent.value
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
    getCarentre();
    getCardeent("1", "1", "1", "1", "1", "1");
  
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
  width: 85%;
  height: 250px;
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
  overflow: hidden;
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
  overflow: hidden;
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