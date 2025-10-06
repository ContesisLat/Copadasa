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
  guia: string
  items: number | null
  peso: string
  naturaleza: string
  destinatario: string
}

const props = defineProps({
  operador: String,
  matricula: String,
  num_vuelo: String,
  puertoE: String,
  puertoD: String,
  aeronave: String,
  tabla: {
    type: Array as PropType<Registro[]>,
    required: true,
    default: () => [],
  },
})

const matricula_aeronave = computed(() => `${props.aeronave} ${props.matricula}`);

const envio_data = computed(() => ({
  operador: props.operador,
  aeronave_matricula: matricula_aeronave.value,
  puerto_despacho: props.puertoE,
  puerto_destino: props.puertoD,
  fecha: dateTimeStore.formattedDate,
  no_vuelo: props.num_vuelo,
  tabla: props.tabla,
}));

// Método para generar el Excel
const generateExcel = async () => {
  try {
    const response = await axios.post(
      dUrl.urlGlobal + '/api2/Regmani_excel',
      envio_data.value,
      { responseType: 'blob' }
    );
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'cargo_manifiesto.xlsx');
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