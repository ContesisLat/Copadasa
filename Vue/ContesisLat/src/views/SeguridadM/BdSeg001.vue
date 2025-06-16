<template>

  <body>
    <div class="Card">
      <section class="layout">
        <div class="header">
          <div class="row">
            <div class="col">
              <div class="btn-group">
                <button class="btn-insert" @click="startInsert" :disabled="isSearching || isEditing || isDeleting">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-upload" viewBox="0 0 16 16">
                    <path
                      d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5" />
                    <path
                      d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708z" />
                  </svg>
                </button>
                <button class="btn-search" @click="startSearch" :disabled="isInserting || isEditing || isDeleting">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-search" viewBox="0 0 16 16">
                    <path
                      d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0" />
                  </svg>
                </button>
                <button class="btn-update" @click="startUpdate" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-pencil-square" viewBox="0 0 16 16">
                    <path
                      d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                    <path fill-rule="evenodd"
                      d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z" />
                  </svg>
                </button>
                <button class="btn-delete" @click="starDelete" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-trash3" viewBox="0 0 16 16">
                    <path
                      d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5M11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47M8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5" />
                  </svg>
                </button>
              </div>
            </div>
            <div class="col">
              <div class="btn-group">
                <button class="btn-next" @click="goToNext" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-caret-right-fill" viewBox="0 0 16 16">
                    <path
                      d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z" />
                  </svg>
                </button>
                <button class="btn-prev" @click="goToPrev" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-rewind-fill" viewBox="0 0 16 16">
                    <path
                      d="M8.404 7.304a.802.802 0 0 0 0 1.392l6.363 3.692c.52.302 1.233-.043 1.233-.696V4.308c0-.653-.713-.998-1.233-.696z" />
                    <path
                      d="M.404 7.304a.802.802 0 0 0 0 1.392l6.363 3.692c.52.302 1.233-.043 1.233-.696V4.308c0-.653-.713-.998-1.233-.696z" />
                  </svg>
                </button>
                <button class="btn-skipstar" @click="goToFirst" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-skip-start-fill" viewBox="0 0 16 16">
                    <path
                      d="M4 4a.5.5 0 0 1 1 0v3.248l6.267-3.636c.54-.313 1.232.066 1.232.696v7.384c0 .63-.692 1.01-1.232.697L5 8.753V12a.5.5 0 0 1-1 0z" />
                  </svg>
                </button>
                <button class="btn-skipend" @click="goToLast" :disabled="!canNavigate">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                    class="bi bi-skip-end-fill" viewBox="0 0 16 16">
                    <path
                      d="M12.5 4a.5.5 0 0 0-1 0v3.248L5.233 3.612C4.693 3.3 4 3.678 4 4.308v7.384c0 .63.692 1.01 1.233.697L11.5 8.753V12a.5.5 0 0 0 1 0z" />
                  </svg>
                </button>
              </div>
            </div>
            <div class="col align-self-end">
            </div>
          </div>
        </div>
        <div class="container">
          <div class="row" style="gap: 20px;">
            <div class="col-9 d-flex flex-column justify-content-center align-items-center">
              <form class="row g-3">
                <div class="col-md-5">
                  <label for="validationDefault01" class="form-label">Base de Datos</label>
                  <input v-model="formData.base_datos" type="text" class="form-control" :readonly="onlyRead">
                </div>
                <div class="col-md-4">
                  <label for="validationDefault04" class="form-label">Tipo de Base de Datos</label>
                  <select v-model="formData.tipo_base_datos" class="form-select" :disabled="onlyRead">
                    <option selected>{{ formData.tipo_base_datos }}</option>
                    <option value="1">Informix</option>
                    <option value="2">Oracle</option>
                    <option value="3">SQL SERVER</option>
                    <option value="4">Sybase</option>
                  </select>
                </div>
                <div class="col-md-6">
                  <label for="validationDefault03" class="form-label">Servidor de Base de Datos</label>
                  <input v-model="formData.servidor_bdatos" type="text" class="form-control" :readonly="onlyRead">
                </div>
                <div class="col-md-6">
                  <label for="validationDefault03" class="form-label">Nombre del equipo</label>
                  <input v-model="formData.hostname" type="text" class="form-control" :readonly="onlyRead">
                </div>
                <div class="col-md-4">
                  <label for="validationDefault02" class="form-label">Direccion</label>
                  <input v-model="formData.ip_address" type="text" class="form-control" :readonly="onlyRead">
                </div>
                <div class="col-md-3">
                  <label for="validationDefault05" class="form-label">Servicio</label>
                  <input v-model="formData.servicio" type="text" class="form-control" :readonly="onlyRead">
                </div>
                <div class="col-md-3">
                  <label for="validationDefault03" class="form-label">Puerto</label>
                  <input v-model="formData.puerto" type="text" class="form-control" :readonly="onlyRead">
                </div>
                <div class="col-md-5">
                  <label for="validationDefault03" class="form-label">Protocolo</label>
                  <input v-model="formData.protocolo" type="text" class="form-control" :readonly="onlyRead">
                </div>
              </form>
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
import { ref, computed } from 'vue';
import axios from 'axios';
import { useAlert } from '@/store/useAlert';
const {success, error, question,warning} = useAlert()
import { UrlGlobal } from '@/store/dominioGlobal';
const dUrl = UrlGlobal()

//--------------------------------------------------------------------------------------------------------------
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
let pk : string
const startUpdate = () => {
  isEditing.value = true;
  isInserting.value = false;
  isSearching.value = false;
  isDeleting.value = false;
  canNavigate.value = false;
  onlyRead.value = false;
  ButtonText.value = 'Editar';
  ButtonText2.value = 'Volver';
  pk = formData.value.base_datos
};

//funcion para iniciar eliminacion
const starDelete = () => {
  isDeleting.value = true;
  isEditing.value = false;
  isInserting.value = false;
  isSearching.value = false;
  canNavigate.value = false;
  onlyRead.value = true;
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
      filters: { base_datos: pk }, // Filtro para identificar el registro a actualizar
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