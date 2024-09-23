<template>

  <body>
      <div class="Card">
          <section class="layout">
              <div class="header">
              </div>
              <div class="container">
                  <div class="row">
                      <div class="col d-flex flex-column justify-content-center align-items-center">
                          <h3><strong>Tarifas de Manejo de Carga</strong></h3>
                          <div class="card overflow-scroll">
                              <table class="table table-hover table-sm">
                                  <thead>
                                      <tr>
                                          <th>Fecha Inicio</th>
                                          <th>Fecha Final</th>
                                          <th>Cargo</th>
                                          <th>Descripcion</th>
                                          <th>Aplica</th>
                                          <th>Valor</th>
                                          <th>Estado</th>e
                                      </tr>
                                  </thead>
                                  <tbody>
                                      <tr v-for="elm in tarifa" :key="elm.tarifa">
                                          <td>{{ elm.fecha_inicio }}</td>
                                          <td>{{ elm.fecha_final }}</td>
                                          <td>{{ elm.cargo }}</td>
                                          <td>{{ elm.nom_cargo }}</td>
                                          <td>{{ elm.aplica }}</td>
                                          <td>{{ elm.valor }}</td>
                                          <td>{{ elm.status }}</td>
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
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { Cartarman } from '@/interface/interfaces'

const tarifa = ref<Array<Cartarman>>([]);

const getTarifa = () => {
axios.get('http://103.23.61.168/api2/cartarman/')
  .then(response => {
    tarifa.value = response.data;
  })
  .catch(error => {
    console.error('Error al buscar Tarifas:', error);
  });
};



onMounted(() => {
getTarifa();
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
  grid-area: header;
}

.container {
  grid-area: container;
}

.card {
  width: 85%;
  height: 250px;
  min-width: min-content;
  min-height: min-content;
  box-sizing: border-box;
}
</style>