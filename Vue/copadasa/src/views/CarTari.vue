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
                      <th>Unidad/Medida</th>
                      <th>Costo/Diario/UMedida</th>
                      <th>Mínimo Diario</th>
                      <th>Full Pallet</th>
                      <th>Estado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="elm in filteredCarga" :key="elm.fecha_inicio">
                      <td>{{ elm.fecha_inicio }}</td>
                      <td>{{ elm.fecha_final }}</td>
                      <td>{{ elm.entrada }}</td>
                      <td>{{ elm.medida }}</td>
                      <td>{{ elm.costo_diario }}</td>
                      <td>{{ elm.minimo_diario }}</td>
                      <td>{{ elm.full_pallet }}</td>
                      <td>{{ elm.nom_status }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </body>
</template>

<script lang="ts" setup>
import { ref, onMounted,computed } from 'vue';
import axios from 'axios';
import { Cartari } from '@/interface/interfaces'
import { UrlGlobal } from '@/store/dominioGlobal';

const dUrl = UrlGlobal()

const tarifa = ref<Array<Cartari>>([]);
const search = ref('')

const getTarifa = (id_tarifa: any) => {
  axios.get(`${dUrl.urlGlobal}/api2/cartari?id_tarifa=${id_tarifa}`)
    .then(response => {
      tarifa.value = response.data;
    })
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