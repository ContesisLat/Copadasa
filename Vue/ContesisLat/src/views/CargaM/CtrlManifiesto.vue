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
              <div class="row" style="gap: 20px;">
                <div class="col d-flex flex-column justify-content-center align-item-center">
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
                                  <th>Piezas</th>
                                  <th>Peso Kg</th>
                                  <th>Aeronave</th>
                                  <th>Matrícula</th>
                                  <th>Estado</th> 
                              </tr>
                          </thead>
                            <tbody>
                              <tr v-for="elm in filteredCarga1" :key="elm.numero_vuelo"
                                  @click="getCardmani(elm.numero_vuelo, elm.operador, elm.fecha)">
                                  <td>{{ elm.fecha }}</td>
                                  <td>{{ elm.nom_operador }}</td>
                                  <td>{{ elm.numero_vuelo }}</td>
                                  <td>{{ elm.nom_pto_despacho }}</td>
                                  <td>{{ elm.nom_pto_destino }}</td>
                                  <td>{{ elm.tot_piezas }}</td>
                                  <td>{{ elm.peso_kg }}</td>
                                  <td>{{ elm.nom_aeronave }}</td>
                                  <td>{{ elm.matricula }}</td>
                                  <td>{{ elm.nom_status }}</td>
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
                                  <th>Remitente</th>
                                  <th>Destinatario</th>
                                  <th>Estado</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="elm in filteredCarga2" :key="elm.no_embarque">
                                  <td>{{ elm.secuencia }}</td>
                                  <td>{{ elm.no_embarque }}</td>
                                  <td>{{ elm.nom_naturaleza }}</td>
                                  <td>{{ elm.cant_items }}</td>
                                  <td>{{ elm.peso_kg }}</td>
                                  <td>{{ elm.remitente }}</td>
                                  <td>{{ elm.destinatario }}</td>
                                  <td>{{ elm.nom_status}}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div> 
                <div class="col"
                  style=" background-color:rgba(255, 255, 255, 0.3);  backdrop-filter: blur(10px); border-radius: 10px;">
                  <div class="btn-group2">
                    <button type="button" class="btn btn-light" @click="toggleSearch" :disabled="!canUseGroup2">{{
                      ButtonText }}</button>
                    <button type="button" class="btn btn-light" @click="resetAll" :disabled="!canUseGroup2">{{ ButtonText2
                    }}</button>
                  </div>
                </div>
              </div>
          </div>
      </section>
    </div>
  </body>
</template>

<script lang="ts" setup>
import { ref, onMounted, computed, Ref } from 'vue';
import axios from 'axios';
import { useAlert } from '@/store/useAlert';
const {success, error, question,warning} = useAlert()
import { UrlGlobal } from '@/store/dominioGlobal';
const dUrl = UrlGlobal()
const search = ref('')
const options = ref('')
import { Carcmani, Cardmani } from '@/interface/interfaces';

//--------------------------------------------------------------------------------------------------------------
const carcmani = ref<Array<Carcmani>>([]);

const getCarcmani = () => { 
        axios.get(dUrl.urlGlobal +'/api2/carcmani/')
            .then(response => {
                carcmani.value = response.data;
        
            //let almacen = response.data.almacen
            //let area = response.data.area

            })
            .catch(error => {
                console.error('Error fetching cargos:', error);
            });
};
//----------------------------------------------------------------
const cardmani = ref<Array<Cardmani>>([])
const getCardmani = (id_numero_vuelo: any, id_operador: any, id_fecha: any) => {
     
        axios.get(`${dUrl.urlGlobal}/api2/carcmani/cardmani?id_numero_vuelo=${id_numero_vuelo}&id_fecha=${id_fecha}`)
            .then(response => { console.log(response.data)
                cardmani.value = response.data; 
     
            })
            .catch(error => {
                console.error('Error fetching loganaquel:', error);
        });
    }
//};
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
                elm.nom_status?.toLowerCase().includes(searchTerm)
            );
        });
    }else{
        return carcmani.value
    }
});
//----------------------------------------------------------------
const filteredCarga2 = computed(() => {
    if (search.value === '') {
        return cardmani.value;

    } else if (options.value == 'Detalle Manifiestos') {
        const searchTerm = search.value.toLowerCase();

        return cardmani.value.filter(elm => {
            return (
                elm.secuencia?.toLowerCase().includes(searchTerm) ||
                elm.no_embarque?.toLowerCase().includes(searchTerm) ||
                elm.nom_naturaleza?.toLowerCase().includes(searchTerm) ||
                elm.remitente?.toLowerCase().includes(searchTerm) ||
                elm.destinatario?.toLowerCase().includes(searchTerm) ||
                elm.cant_items?.toLowerCase().includes(searchTerm) ||
                elm.peso_kg?.toLowerCase().includes(searchTerm) ||
                elm.nom_status?.toLowerCase().includes(searchTerm) 
            );
        });
    }else{
        return cardmani.value
    }
});
//----------------------------------------------------------------
// Estado del formulario y la data
const formData = ref({
  base_datos: '',
  tipo_base_datos: '',
  servidor_bdatos: '',
  hostname: '',
  ip_address: '',
  servicio: '',
  puerto: '',
  protocolo: ''
});

// Variables de control
const dataList = ref<any[]>([]); // Lista de datos de la API
const currentIndex = ref(0);
const isEditing = ref(false);
const isSearching = ref(false);
const isInserting = ref(false);
const isDeleting = ref(false)
const canNavigate = ref(false);
const onlyRead = ref(true);
const ButtonText = ref('OK')
const ButtonText2 = ref('Cancelar')

// Deshabilita los botones de btn-group2 si no está en modo búsqueda o insercion
const canUseGroup2 = computed(() => isSearching.value || isInserting.value || isEditing.value || isDeleting.value);

//------------------------------------------------------------------------------------------------------------------

//Funciones---------------------------------------------------------------------------------------------------------
// Función para iniciar inserción
const startInsert = () => {
  isInserting.value = true;
  isSearching.value = false;
  isEditing.value = false;
  isDeleting.value = false;
  onlyRead.value = false;
  ButtonText.value = 'Insertar';
};

// Función para iniciar búsqueda
const startSearch = () => {
  isSearching.value = true;
  isInserting.value = false;
  isEditing.value = false;
  isDeleting.value = false;
  onlyRead.value = false;
};

// Funcion para iniciar edición
const startUpdate = () => {
  isEditing.value = true;
  isInserting.value = false;
  isSearching.value = false;
  isDeleting.value = false;
  canNavigate.value = false;
  onlyRead.value = false;
  ButtonText.value = 'Editar';
  ButtonText2.value = 'Volver';
};

//funcion para iniciar eliminacion
const starDelete = () => {
  isDeleting.value = true;
  isEditing.value = false;
  isInserting.value = false;
  isSearching.value = false;
  canNavigate.value = false;
  onlyRead.value = false;
  ButtonText.value = 'Eliminar';
  ButtonText2.value = 'Volver'
};

// Función para hacer la consulta
const handleSearch = async () => {
  try {
    const response = await axios.post(dUrl.urlGlobal + '/api/query', { tabla: 'segbdato', filtro: formData.value });
    dataList.value = response.data;
    currentIndex.value = 0;
    updateFormData();

    if (dataList.value.length === 0) {
      warning('No se ha encontrado registros con los datos ingresados','Vuelva hacer la consulta')
      ButtonText.value = 'Ok';
    } else {
      ButtonText.value = 'Consulta';
      canNavigate.value = true;
      onlyRead.value = true;
    }
  } catch (err:any) {
    error(err.response?.data?.detail || 'Ocurrió un error en la consulta.')
  }
};

//Funcion para la insercion
const handleInsert = async () => {
    // Mostrar confirmación
    const result = await question(
    'Se va a insertar el campo con los nuevos datos.',
    '¿Deseas insertar este registro?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }
  
  const data = {
    model: "segbdato",
    data: {
      base_datos: formData.value.base_datos,
      tipo_base_datos: formData.value.tipo_base_datos,
      servidor_bdatos: formData.value.servidor_bdatos,
      hostname: formData.value.hostname,
      ip_address: formData.value.ip_address,
      servicio: formData.value.servicio,
      puerto: formData.value.puerto,
      protocolo: formData.value.protocolo
    }
  }
  try {
    const response = await fetch(dUrl.urlGlobal + '/api/insert/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
   
    if (response.ok) {
       success('Los datos fueron insertados correctamente.', 'Insercion exitosa')
    } else{
       error('Ocurrió un error al insertar los datos.')
    }
  } catch (err:any ) {
    error(err.response?.data?.detail || 'Ocurrió un error al insertar los datos.')
  }
}

//funcion para el update
const handleUpdate = async () => {
    // Mostrar confirmación
    const result = await question(
    'Se va a actualizar el campo con los nuevos datos.',
    '¿Deseas actualizar este registro?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }

  try {
    const response = await axios.post(dUrl.urlGlobal + '/api/update/', {
      table: 'segbdato',
      filters: { base_datos: formData.value.base_datos }, // Filtro para identificar el registro a actualizar
      data: {
        base_datos: formData.value.base_datos,
        tipo_base_datos: formData.value.tipo_base_datos,
        servidor_bdatos: formData.value.servidor_bdatos,
        hostname: formData.value.hostname,
        ip_address: formData.value.ip_address,
        servicio: formData.value.servicio,
        puerto: formData.value.puerto,
        protocolo: formData.value.protocolo
      } // Datos a actualizar
    })
    if (response.status == 200) {
        success('Los datos fueron actualizados correctamente.', 'Actualización exitosa')
    } else{
       error('Ocurrió un error al actualizar los datos.')
    }
  } catch (err:any) {
    error(err.response?.data?.detail || 'Ocurrió un error al actualizar los datos.')
  }
}

//funcion para eliminar
const handleDelete = async () => {
   // Mostrar confirmación
   const result = await question(
    '¡No podrás revertir esto!',
    '¿Deseas eliminar este registro?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }

  try {
    const response = await axios.post(dUrl.urlGlobal + '/api/delete/', {
      table: 'segbdato',
      filters: { base_datos: formData.value.base_datos }, // Filtro para identificar el registro a eliminar
    })
    if (response.status == 200) {
       success('¡Eliminado!', 'El registro ha sido eliminado con exito.')
    } else{
       error('Ocurrió un error al eliminar el registro.')
    }
  } catch (err:any) {
    error(err.response?.data?.detail || 'Ocurrió un error al eliminar el registro.')
  }
}

// Actualiza el formulario con el registro actual
const updateFormData = () => {
  if (dataList.value.length > 0) {
    formData.value = { ...dataList.value[currentIndex.value] };
  }
};
//------------------------------------------------------------------------------------------------------------------

// Navegación entre registros---------------------------------------------------------------------------------------
const goToFirst = () => {
  currentIndex.value = 0;
  updateFormData();
};
const goToPrev = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--;
    updateFormData();
  }
};
const goToNext = () => {
  if (currentIndex.value < dataList.value.length - 1) {
    currentIndex.value++;
    updateFormData();
  }
};
const goToLast = () => {
  currentIndex.value = dataList.value.length - 1;
  updateFormData();
};
//------------------------------------------------------------------------------------------------------------------

// Control de botones submit y cancelar-----------------------------------------------------------------------------------------------

//boton principal que controla el submit
const toggleSearch = () => {
  if (dataList.value.length && isSearching.value == true) {
    // Si ya hay datos, "Consulta" limpia y reinicia la búsqueda
    dataList.value = [];
    formData.value = { base_datos: '', tipo_base_datos: '', servidor_bdatos: '', hostname: '', ip_address: '', servicio: '', puerto: '', protocolo: '', };
    onlyRead.value = false;
    ButtonText.value = 'Ok'
    canNavigate.value = false;
  } else if (isInserting.value == true) {
    handleInsert();
  } else if (isEditing.value == true) {
    handleUpdate();
  } else if (isDeleting.value == true) {
    handleDelete()
  }
  else {
    // Si no hay datos, hace la consulta
    handleSearch();
  }
};


// Boton que restablece todo a estado inicial
const resetAll = () => {
  if (ButtonText2.value == 'Cancelar') {
    dataList.value = [];
    formData.value = { base_datos: '', tipo_base_datos: '', servidor_bdatos: '', hostname: '', ip_address: '', servicio: '', puerto: '', protocolo: '', };
    isInserting.value = false;
    isSearching.value = false;
    isEditing.value = false;
    isDeleting.value = false;
    canNavigate.value = false;
    onlyRead.value = true;
    ButtonText.value = 'Ok'
  } else {
    dataList.value = [];
    formData.value = { base_datos: '', tipo_base_datos: '', servidor_bdatos: '', hostname: '', ip_address: '', servicio: '', puerto: '', protocolo: '', };
    startSearch()
    ButtonText.value = 'Ok'
    ButtonText2.value = 'Cancelar'
  }

};
//------------------------------------------------------------------------------------------------------------------
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
}

.btn-group2 button:active {
  transform: scale(0.95);
}
</style>