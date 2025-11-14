<template>


  <button type="button" class="btn btn-light" @click="generateExcel">
    Generar Excel
  </button>


</template>

<script setup lang="ts">
import { computed, PropType, ref, defineProps } from 'vue';
import axios from 'axios';
import { useDateTimeStore } from '@/store/dateTimeStore';
import { UrlGlobal } from '@/store/dominioGlobal';

const dUrl = UrlGlobal()
const dateTimeStore = useDateTimeStore();

type Registro = {
  cargo: string
  tiempo_total: string 
  monto: string
  status: string
  nom_status: string
}

const props = defineProps({
  fecha: String,
  compania: String,
  matricula: String,
  aeronave: String,
  fecha_llegada: String,
  hora_llegada: String,
  status: String,
   
  tabla: {
    type: Array as PropType<Registro[]>,
    required: true,
    default: () => [],
  },
})

//const matricula_aeronave = computed(() => `${props.fecha} ${props.matricula}`);

const envio_data = computed(() => ({
  fecha: props.fecha,
  compania: props.compania,
  matricula: props.matricula,
  aeronave: props.aeronave,
  fecha_llegada: props.fecha_llegada,
  hora_llegada: props.hora_llegada,
  status: props.status,

  tabla: props.tabla,
}));

// Método para generar el Excel
const generateExcel = async () => {
  try {
    const response = await axios.post(
      dUrl.urlGlobal + '/api2/Caratvue_excel',
      envio_data.value,
      { responseType: 'blob' }
    );
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'servicios_aereos.xlsx');
    document.body.appendChild(link);
    link.click();
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error('Error al generar el manifiesto:', error);
  }
};
</script>

<style scoped>
/* Estilos opcionales para el botón */
button {
  transition: transform 0.2s ease;
}

button:active {
  transform: scale(0.95);
}
</style>