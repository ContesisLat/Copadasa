<template>
  <div class="modal-backdrop"></div>

  <div class="ReportPage">

    <h4>Generar Reporte</h4>
    <hr>

    <div class="row w-100">

      <!-- FORMULARIO IZQUIERDO -->
      <div class="col-9">

        <form class="row g-3 needs-validation" novalidate>

          <div class="row mb-1">
            <label class="col-sm-3 col-form-label col-form-label-sm">Fecha Desde</label>
            <div class="col-sm-4">
              <input type="date" v-model="fecha_desde" class="form-control">
            </div>

            <label class="col-sm-3 col-form-label col-form-label-sm">Fecha Hasta</label>
            <div class="col-sm-4">
              <input type="date" v-model="fecha_hasta" class="form-control">
            </div>
          </div>

          <div class="row mb-1">
            <label class="col-sm-3 col-form-label col-form-label-sm">Transac.</label>
            <div class="col-sm-6">
              <select class="form-select form-select-sm" v-model="codigo">
                <option selected>{{ descripcionCodigo }}</option>
                <option v-for="op in codigos" :key="op.codigo" :value="op.codigo">
                  {{ op.descripcion }}
                </option>
              </select>
            </div>
          </div>

          <div class="row mb-1">
            <label class="col-sm-3 col-form-label col-form-label-sm">Cliente</label>
            <div class="col-sm-7">
              <select class="form-select form-select-sm" v-model="cliente">
                <option selected>{{ descripcionCliente }}</option>
                <option v-for="op in clientes" :key="op.cliente" :value="op.cliente">
                  {{ op.nombre_comercial }}
                </option>
              </select>
            </div>
          </div>

          <div class="row mb-1">
            <label class="col-sm-3 col-form-label col-form-label-sm">Documento</label>
            <div class="col-sm-4">
              <input type="text" v-model="documento" class="form-control">
            </div>
          </div>

          <div class="row mb-1">
            <div class="col-sm-4">
              <label class="form-label">Estado</label>
              <select class="form-select form-select-sm" v-model="status">
                <option value="I">Ingresadas</option>
                <option value="C">Calculada</option>
                <option value="E">Entregadas</option>
              </select>
            </div>
          </div>

        </form>
      </div>

      <!-- BOTONES DERECHA -->
      <div class="col-3 d-flex align-items-start justify-content-end">
        <div style="
            width: 200px;
            background-color: rgba(255,255,255,0.3);
            backdrop-filter: blur(10px);
            border-radius: 10px;
            padding: 15px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            overflow: hidden;
          ">
          <button type="button" class="btn btn-light" @click="generateExcel">
            Generar Excel
          </button>

          <button type="button" class="btn btn-light" @click="handleClick">
            Cancelar
          </button>
        </div>
      </div>

    </div>

  </div>
</template>


<script setup lang="ts">
import { computed, PropType, ref, defineProps, defineEmits, onMounted } from 'vue';
import axios from 'axios';
const { error, success } = useAlert()
import { useDateTimeStore } from '@/store/dateTimeStore';
import { UrlGlobal } from '@/store/dominioGlobal';
import { useAlert } from '@/store/useAlert';

const dUrl = UrlGlobal()
const dateTimeStore = useDateTimeStore();

const props = defineProps({
  btnEx: Boolean

})

const emits = defineEmits(['insertProps'])
const handleClick = () => {
  emits("insertProps", !props.btnEx)
}

const fecha_desde = ref<string>('')
const fecha_hasta = ref<string>('')
const codigo = ref<string>('')
const cliente = ref<string>('')
const documento = ref<string>('')
const status = ref<string>('')
//const matricula_aeronave = computed(() => `${props.fecha} ${props.matricula}`);

const envio_data = computed(() => ({
  fecha_desde: fecha_desde.value,
  fecha_hasta: fecha_hasta.value,
  codigo: codigo.value,
  cliente: cliente.value,
  documento: documento.value,
  status: status.value
}));

// Método para generar el Excel
const generateExcel = async () => {
  if (!fecha_desde.value) {
    error('Debe digitar la fecha inicial...')
    return
  }
  if (!fecha_hasta.value) {
    error('Debe digitar la fecha final...')
    return
  }

  if (fecha_desde.value > fecha_hasta.value) {
    error('Fecha inicial no puede ser mayor que la fecha final...')
    return
  }

  try {
    const response = await axios.post(
      dUrl.urlGlobal + '/api2/Logctmo_excel',
      envio_data.value,
      { responseType: 'blob' }
    );
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'movimientos_ctofrio.xlsx');
    document.body.appendChild(link);
    link.click();
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error('Error al generar el manifiesto:', error);
  }
};

const codigos = ref<any[]>([]);
const clientes = ref<any[]>([])
onMounted(async () => {
  const responseN = await axios.get(dUrl.urlGlobal + '/api2/logtral/filter?status=A')
  codigos.value = responseN.data

  const responseC = await axios.get(dUrl.urlGlobal + '/api2/crmclte/filter?status=A')
  clientes.value = responseC.data
})
//computados de las ayudas
const descripcionCodigo = computed(() => {
  const encontrado = codigos.value.find(op => op.codigo === codigo.value)
  return encontrado ? encontrado.descripcion : ''
})

const descripcionCliente = computed(() => {
  const encontrado = clientes.value.find(op => op.cliente === cliente.value)
  return encontrado ? encontrado.nombre_comercial : ''
})

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Estilos opcionales para el botón */
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
  @media screen and (max-width:600px) {
    width: 500px;
  }
}

.ReportPage {
  max-height: 70%;
  width: 90%;
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
  overflow: auto;

  @media screen and (max-width: 600px) {
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

button {
  transition: transform 0.2s ease;
}

button:active {
  transform: scale(0.95);
}

.btn-group2 button:active {
  transform: scale(0.80);
}

.div-buttom {
  max-width: 200px;
  overflow: hidden;
}
</style>