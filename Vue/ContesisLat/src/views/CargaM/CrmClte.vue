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
          </div>
        </div>
        <div class="container">
          <div class="row" style="gap: 20px;">
            <div class="col-10 d-flex flex-column justify-content-center align-items-center" style="gap: 50px;">
              <div class="row">
                <form>
                  <h3>Catálogo de Clientes</h3>
                  <div class="row mb-1">
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Cliente</label>
                    <div class="col-sm-2">
                      <input class="form-control form-control-sm" v-model="formData.cliente" :readonly="onlyRead">
                    </div>
                    
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Estado</label>
                    <div class="col-sm-2">
                      <select class="form-select form-select-sm" v-model="formData.status" :disabled="onlyRead">
                        <option>{{ formData.status }}</option>
                        <option value='A'>Activo</option>
                        <option value='I'>Inactivo</option>
                      </select>
                    </div>
                  </div>
                  <div class="row mb-1">
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Tipo Cliente</label>
                    <div class="col-sm-2">
                      <select class="form-select form-select-sm" v-model="formData.code_id" :disabled="onlyRead">
                        <option>{{ formData.code_id }}</option>
                        <option value="J" selected>Jurídico</option>
                        <option value="N">Natural</option>
                      </select>
                      </div>
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Nombre Comercial</label>
                    <div class="col-sm-7">
                      <input class="form-control form-control-sm" v-model="formData.nombre_comercial" :readonly="onlyRead">
                    </div>
                  </div>
                  <div class="row mb-1">
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Razón Social</label>
                    <div class="col-sm-5">
                      <input class="form-control form-control-sm" v-model="formData.razon_social" :readonly="onlyRead">
                    </div>
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Ruc</label>
                    <div class="col-sm-3">
                      <input class="form-control form-control-sm" v-model="formData.id_legal" :readonly="onlyRead">
                    </div>
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Dv.</label>
                    <div class="col-sm-1">
                      <input class="form-control form-control-sm" v-model="formData.digito_vf" :readonly="onlyRead">
                    </div>
                  </div>
                  <div class="row mb-1">
                    <label for="inputPassword4" class="col-sm-1 col-form-label col-form-label-sm">Dirección</label>
                    <div class="col-sm-6">
                      <input class="form-control form-control-sm" v-model="formData.barrio" :readonly="onlyRead">
                    </div>
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Ubicación</label>
                    <div class="col-sm-2">
                      <input class="form-control form-control-sm" v-model="formData.ubicacion" :readonly="onlyRead">
                    </div> 
                  </div>
                  <div class="row mb-1">
                    <label for="inputPassword4" class="col-sm-1 col-form-label col-form-label-sm">Email</label>
                    <div class="col-sm-6">
                      <input class="form-control form-control-sm" v-model="formData.email" :readonly="onlyRead">
                    </div>
                  </div>
                  <div class="row mb-1">
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Teléfono #1</label>
                    <div class="col-sm-2">
                      <input class="form-control form-control-sm" v-model="formData.telefono1" :readonly="onlyRead">
                    </div>
                    <label for="inputPassword2" class="col-sm-1 col-form-label col-form-label-sm">Teléfono #2</label>
                    <div class="col-sm-2">
                      <input class="form-control form-control-sm" v-model="formData.telefono2" :readonly="onlyRead">
                    </div>
                  </div>
                </form>
              </div>
            </div>
            <div class="col"
              style=" background-color:rgba(255, 255, 255, 0.3);  backdrop-filter: blur(10px); border-radius: 10px;">
              <div class="btn-group2">
                <button type="button" class="btn btn-light btn-sm" @click="toggleSearch" :disabled="!canUseGroup2">{{
                  ButtonText }}</button>
                <button type="button" class="btn btn-light btn-sm" @click="resetAll" :disabled="!canUseGroup2">{{
                  ButtonText2 }}</button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </body>
</template>

<script lang="ts" setup>
import { ref, watch, computed,onMounted } from 'vue'
import axios from 'axios';
import { useAlert } from '@/store/useAlert';
const { success, error, question, warning } = useAlert()
import { UrlGlobal } from '@/store/dominioGlobal';
import { userGlobalStore } from '@/store/userGlobal';
import { useDateTimeStore } from '@/store/dateTimeStore';
import { RefSymbol } from '@vue/reactivity';

const dUrl = UrlGlobal()
const userStore = userGlobalStore()
const dateTimeStore = useDateTimeStore();

//--------------------------------------------------------------------------------------------------------------
// Estado del formulario y la data
const formData = ref({
  cliente: '',
  code_id: '',
  status: '',
  nombre_comercial: '',
  razon_social: '',
  id_legal: '',
  digito_vf: '',
  ubicacion: '',
  barrio: '',
  telefono1: '',
  telefono2: '',
  email: '',
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
const tonlyRead = ref(true);
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
  tonlyRead.value = false
  ButtonText.value = 'Insertar';
  formData.value.status = 'A'
  formData.value.code_id ='J'
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
let pk: string
const startUpdate = () => {
  isEditing.value = true;
  isInserting.value = false;
  isSearching.value = false;
  isDeleting.value = false;
  canNavigate.value = false;
  onlyRead.value = false;
  ButtonText.value = 'Editar';
  ButtonText2.value = 'Volver';
  pk = formData.value.cliente
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
    const response = await axios.post(dUrl.urlGlobal + '/api2/query', { tabla: 'crmclte', filtro: formData.value });
    dataList.value = response.data;
    currentIndex.value = 0;
    updateFormData();

    if (dataList.value.length === 0) {
      warning('No se ha encontrado registros con los datos ingresados', 'Vuelva hacer la consulta')
      ButtonText.value = 'Ok';
    } else {
      ButtonText.value = 'Consulta';
      canNavigate.value = true;
      onlyRead.value = true;
    }
  } catch (err: any) {
    error(err.response?.data?.detail || 'Ocurrió un error en la consulta.')
  }
};

 

//Funcion para la insercion
const handleInsert = async () => {
  let vali = 0

// Validar Campos
  if(!formData.value.cliente){
    error('Digite el código del Cliente')
    return
  }

  if (!formData.value.nombre_comercial) {
    error('Digite el nombre comercial... ')
    return
  }

  if (!formData.value.code_id) {
    error('Defina el tipo de cliente... ')
    return
  }

  if (!formData.value.razon_social) {
    error('Digite la razón social del cliente... ')
    return
  }

  if (!formData.value.id_legal) {
    error('Digite el Ruc o cédula... ')
    return
  }

  if (!formData.value.digito_vf) {
    error('Debe digitar el dígito verificador... ')
    return
  }

  if (!formData.value.email) {
    error('Tiene que digitar el correo electrónico...')
    return
  }
  if (!formData.value.status) {
    error('Estado del Cliente incorrecto...')
    return
  }

  if (!formData.value.telefono1 && !formData.value.telefono2) {
    error('Debe digitar al menos un número telefónico... ')
    return
  }

 
  // VALIDA REGISTRO DUPLICADO
  try {
    const response = await axios.post(dUrl.urlGlobal + '/api2/query', { tabla: 'crmclte', 
        filtro: { id_legal: formData.value.id_legal}});

    dataList.value = response.data;

    if (dataList.value.length > 0) {
      warning('Este Ruc o cédula ya existe... ', 'valide la Información')
      return
    }

    } catch (err: any) {
        error(err.response?.data?.detail || 'Ocurrió un error en la consulta.')
  }

  const result = await question(
    'Se va a insertar el campo con los nuevos datos.',
    '¿Deseas insertar este registro?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }

  const data = {
    model: "crmclte",
    data: {
      cliente: formData.value.cliente,
      nombre_comercial: formData.value.nombre_comercial,
      code_id: formData.value.code_id,
      id_legal: formData.value.id_legal,
      digito_vf: formData.value.digito_vf,
      razon_social: formData.value.razon_social,
      ubicacion: formData.value.ubicacion,
      barrio: formData.value.barrio,
      telefono1: formData.value.telefono1,
      telefono2: formData.value.telefono2,
      email: formData.value.email,
      status: formData.value.status,
      creado_por: userStore.globalUser,
      fecha_creado: dateTimeStore.formattedDate,
      hora_creado: dateTimeStore.formattedTime
    }
  }
  try {
    const response = await fetch(dUrl.urlGlobal + '/api2/insert/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })

    if (!response.ok) {
      error('Ocurrió un error al insertar los datos del Cliente', 'Formulario')
    }
    else {
      vali++     
    } 
  } catch (err: any) {
        error(err.response?.data?.detail || 'Error al tratar de Insertar... ')
    }

  if (vali > 0) {
    success('Los datos fueron insertados correctamente.', 'Registro exitoso')
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
    const response = await axios.post(dUrl.urlGlobal + '/api2/update/', {
      table: 'crmclte',
      filters: { cliente: formData.value.cliente }, // Filtro para identificar el registro a actualizar
      data: {
      cliente: formData.value.cliente,
      nombre_comercial: formData.value.nombre_comercial,
      code_id: formData.value.code_id,
      id_legal: formData.value.id_legal,
      digito_vf: formData.value.digito_vf,
      razon_social: formData.value.razon_social,
      ubicacion: formData.value.ubicacion,
      barrio: formData.value.barrio,
      telefono1: formData.value.telefono1,
      telefono2: formData.value.telefono2,
      email: formData.value.email,
      status: formData.value.status,
      creado_por: userStore.globalUser,
      fecha_creado: dateTimeStore.formattedDate,
      hora_creado: dateTimeStore.formattedTime
    } // Datos a actualizar
    })
    if (response.status == 200) {
      success('Los datos fueron actualizados correctamente.', 'Actualización exitosa')
    } else {
      error('Ocurrió un error al actualizar los datos.')
    }
  } catch (err: any) {
    error(err.response?.data?.detail || 'Ocurrió un error al actualizar los datos.')
  }
}

//funcion para eliminar
const handleDelete = async () => {
 // Mostrar confirmación
  const result = await question(
    'Se va inactivar el registro.',
    '¿Deseas inhabilitar a este registro?'
  )

  if (!result.isConfirmed) {
    // Usuario canceló, salimos de la función
    return
  }

  try {
    const response = await axios.post(dUrl.urlGlobal + '/api2/update/', {
      table: 'crmclte',
      filters: { cliente: formData.value.cliente }, // Filtro para identificar el registro a actualizar
      data: {
        status: 'I',
      }
    })
    if (response.status == 200) {
      success('el registro fue inhabilitado correctamente.', 'Accion exitosa')
    } else {
      error('Ocurrió un error al inactivar el registro.')
    }
  } catch (err: any) {
    error(err.response?.data?.detail || 'Ocurrió un error inesperado.')
  }
}

// Actualiza el formulario con el registro actual
const updateFormData = () => {
  if (dataList.value.length > 0) {
    formData.value = { ...dataList.value[currentIndex.value] };
  }
};
     
//carga de las ayudas
const operadores = ref<any[]>([]);
const aeronaves = ref<any[]>([]);
const puertos = ref<any[]>([]);
const naturaleza = ref<any[]>([]);
onMounted(async () => {
  const responseO = await axios.get(dUrl.urlGlobal + '/api2/caropera/')
  operadores.value = responseO.data
  const responseA = await axios.get(dUrl.urlGlobal + '/api2/cartiaero/')
  aeronaves.value = responseA.data
  const responseP = await axios.get(dUrl.urlGlobal + `/api2/puertos/filter?status=A`)
  puertos.value = responseP.data
  const responseN = await axios.get(dUrl.urlGlobal + '/api2/naturaleza/filter?status=A')
  naturaleza.value = responseN.data
})

//computados de las ayudas
const descripcionOperador = computed(() => {
  const encontrado = operadores.value.find(op => op.operador === formData.value)
  return encontrado ? encontrado.nombre : ''
})

const descripcionAeronaves = computed(() => {
  const encontrado = aeronaves.value.find(i => i.aeronave === formData.value)
  return encontrado ? encontrado.descripcion : ''
})

const descripcionPuertosDP = computed(() => {
  const encontrado = puertos.value.find(i => i.puerto === formData.value)
  return encontrado ? encontrado.nombre : ''
})

const descripcionPuertosDT = computed(() => {
  const encontrado = puertos.value.find(i => i.puerto === formData.value)
  return encontrado ? encontrado.nombre : ''
})

const descripcionNaturaleza = (naturalezaId: string) => {
  const encontrado = naturaleza.value.find(i => i.aeronave === naturalezaId)
  return encontrado ? encontrado.nombre : ''
}

let idnaturaleza : any
const idN = (naturalezaId: string) => {
  idnaturaleza = naturalezaId
}
//const descripcionNaturaleza = computed(() => {
//  const encontrado = naturaleza.value.find(i => i.naturaleza === registros.value.)
//  return encontrado ? encontrado.nombre
//})
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
    formData.value = { cliente: '', nombre_comercial: '', razon_social: '', id_legal: '', code_id: '', status: '', 
                      telefono1: '', telefono2: '', email: '', ubicacion: '', digito_vf: '', barrio: '', };
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
    formData.value = { cliente: '', nombre_comercial: '', code_id: '', razon_social: '', id_legal: '', status: '', 
                        digito_vf: '', ubicacion: '', barrio: '', telefono1: '', telefono2: '', email: ''};
    isInserting.value = false;
    isSearching.value = false;
    isEditing.value = false;
    isDeleting.value = false;
    canNavigate.value = false;
    onlyRead.value = true;
    tonlyRead.value = true;
    ButtonText.value = 'Ok'
  } else {
    dataList.value = [];
    formData.value = { cliente: '', nombre_comercial: '', code_id: '', id_legal: '', digito_vf: '', razon_social: '', 
                      status: '', ubicacion: '', barrio: '', telefono1: '', telefono2: '', email: '' };
    startSearch()
    ButtonText.value = 'Ok'
    ButtonText2.value = 'Cancelar'
  }
};
//---------------------------------------------------------------------------------------------------------------------------------------------------------


//control de filas automaticas de la tabla-----------------------------------------------------------------------------------------------------------------

// Función para validar si una fila está completamente llena
 

// Observar el último elemento y agregar uno nuevo si está lleno
 
  

  // Evaluar la última fila
//-----------------------------------------------------------------------------------------------------------------------------------------------------------
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
  overflow: hidden;
}

.btn-group2 button:active {
  transform: scale(0.95);
}

.div-dotted {
  height: 150px;
  position: relative;
  border: 1px dotted whitesmoke;
  display: flex;
  padding: 20px;
  overflow-y: scroll;
}
</style>