<template>
  <body>
    <div class="Card">
      <section class="layout">
        <div class="container">
          <div class="row" style="gap: 20px;">
            <div class="col-10 d-flex flex-column justify-content-center align-items-center" style="gap: 50px;">
              <div class="row">
                <form>
                  <h3><strong>Servicios a Aeronaves</strong></h3>
                  <div class="row mb-1"> <!--Fecha-->
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Fecha Inicial</label>
                    <div class="col-sm-3">
                      <input class="form-control form-control-sm" type="date" v-model="formData.fecha_inicial">
                    </div>
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Fecha Final</label>
                    <div class="col-sm-3">
                      <input class="form-control form-control-sm" type="date" v-model="formData.fecha_final">
                    </div>
                  </div>
                  <div class="row mb-1"> 
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Compañía</label>
                    <div class="col-sm-5"> <!--Tipo Aeronave-->
                      <select class="form-select form-select-sm" v-model="formData.compania">
                        <option selected>{{ descripcionCompania }}</option>
                        <option v-for="i in companias" :key="i.compania" :value="i.compania">{{ i.nombre }}</option>
                      </select>
                    </div>
                  </div>
                  <!--div class="row mb-1"> 
                    <label for="inputPassword3" class="col-sm-1 col-form-label col-form-label-sm">Tipo aeronave</label>
                    <div class="col-sm-3">
                      <select class="form-select form-select-sm" v-model="formData.aeronave" :disabled="onlyRead">
                        <option selected>{{ descripcionAeronaves }}</option>
                        <option v-for="i in aeronaves" :key="i.aeronave" :value="i.aeronave">{{ i.descripcion }}</option>
                      </select>
                    </div>
                  </div-->
                </form>
              </div>
            </div>
            <div class="col"
              style=" background-color:rgba(255, 255, 255, 0.3);  backdrop-filter: blur(10px); border-radius: 10px;">
              <div class="btn-group2">
                <button type="button" class="btn btn-light btn-sm" @click="generateExcel">Generar Excel</button>
                <button type="button" class="btn btn-light btn-sm" @click="Salir">Cancelar</button>
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
import CarCoaer from './CarCoaer.vue';
import { Cartarvue } from '@/interface/interfaces';
import ExRegSerAero from './pImpresion/ExRegSerAero.vue';
import { isReturnStatement } from 'typescript';

const dUrl = UrlGlobal()
const userStore = userGlobalStore()
const dateTimeStore = useDateTimeStore();

const onlyRead = ref(true);
onlyRead.value = true
//--------------------------------------------------------------------------------------------------------------
// Estado del formulario y la data
const formData = ref({
  fecha_inicial: '',
  fecha_final: '',
  compania: '',
  aeronave: '',
});

const envio_data = computed(() => ({
  fecha_inicial: formData.value.fecha_inicial,
  fecha_final: formData.value.fecha_final,
  compania: formData.value.compania,
   
}));

const generateExcel = async () => {
  if (!formData.value.fecha_inicial) {
    error('Digite la fecha inicial del resumen...')
    return
  }
  if (!formData.value.fecha_final) {
    error('Debe digitar la fecha final del resumen...')
    return
  }

  if (formData.value.fecha_inicial > formData.value.fecha_final) {
    error('Fecha inicial del resumen es mayor a la fecha final...')
    return
  }
  
  try {
    const response = await axios.post(
      dUrl.urlGlobal + '/api2/Caratvue_excel_resumen',
      envio_data.value,
      { responseType: 'blob' }
    );
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'serv_aereos_resumen.xlsx');
    document.body.appendChild(link);
    link.click();
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error('Error al generar el manifiesto:', error);
  }
};
//----------------------------------------------------------------
const Salir = () => {
  let i = 0

};
//carga de las ayudas
const aeronaves = ref<any[]>([]);
const companias = ref<any[]>([]);
onMounted(async () => {
  const responseA = await axios.get(dUrl.urlGlobal + '/api2/cartiaero/')
  aeronaves.value = responseA.data
  const responseP = await axios.get(dUrl.urlGlobal + `/api2/compania/filter?status=A`)
  companias.value = responseP.data

//computados de las ayudas
const descripcionAeronaves = computed(() => {
  const encontrado = aeronaves.value.find(i => i.aeronave === formData.value.aeronave)
  return encontrado ? encontrado.descripcion : ''
})

const descripcionCompania = computed(() => {
  const encontrado = companias.value.find(i => i.compania === formData.value.compania)
  return encontrado ? encontrado.nombre : ''
})
});
//---------------------------------------------------------------------------
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