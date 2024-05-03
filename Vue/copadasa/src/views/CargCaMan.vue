<template>

  <body>
      <div class="Card">
          <section class="layout">
              <div class="header">
              </div>
              <div class="container">
                  <div class="row">
                      <div class="col d-flex flex-column justify-content-center align-items-center">
                          <h3><strong>Cargo Por Manejo</strong></h3>
                          <div class="card overflow-scroll">
                              <table class="table table-hover table-sm">
                                  <thead>
                                      <tr>
                                          <th>Cargo</th>
                                          <th>Nombre</th>
                                          <th>Naturaleza</th>
                                          <th>Nombre Naturaleza</th>
                                          <th>Status</th>
                                      </tr>
                                  </thead>
                                  <tbody>
                                      <tr v-for="cargo in cargos" :key="cargo.cargo">
                                          <td>{{ cargo.cargo }}</td>
                                          <td>{{ cargo.nombre }}</td>
                                          <td>{{ cargo.naturaleza }}</td>
                                          <td>{{ getNombreNaturaleza(cargo.naturaleza) }}</td>
                                          <td>{{ cargo.status }}</td>
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

const cargos = ref<Array>([]);
const naturalezas: Record<string, string> = {};

const getCargos = () => {
axios.get('http://127.0.0.1:8000/api2/cargcaman/')
  .then(response => {
    cargos.value = response.data;
  })
  .catch(error => {
    console.error('Error fetching cargos:', error);
  });
};

const getNaturalezas = () => {
axios.get('http://127.0.0.1:8000/api2/carnatur/')
  .then(response => {
    response.data.forEach((naturaleza: { naturaleza: string, nombre: string }) => {
      naturalezas[naturaleza.naturaleza] = naturaleza.nombre;
    });
  })
  .catch(error => {
    console.error('Error fetching naturalezas:', error);
  });
};

const getNombreNaturaleza = (naturalezaId: string) => {
return naturalezas[naturalezaId] || 'N/A';
};

onMounted(() => {
getCargos();
getNaturalezas();
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
.card{
    width: 85%;
    height: 250px;
    min-width:min-content;
    min-height: min-content;
    box-sizing: border-box;
}
</style>