<template>

  <body>
      <div class="Card">
          <section class="layout">
              <div class="header">
              </div>
              <div class="container">
                  <div class="row">
                      <div class="col d-flex flex-column justify-content-center align-items-center">
                          <h3><strong>Cargos por Atención de Vuelos</strong></h3>
                          <div class="card overflow-scroll">
                              <table class="table table-hover table-sm">
                                  <thead>
                                      <tr>
                                          <th>Cargo</th>
                                          <th>Descripción</th>
                                          <th>Estado</th>
                                      </tr>
                                  </thead>
                                  <tbody>
                                      <tr v-for="elm in cargo" :key="elm.naturaleza">
                                          <td>{{ elm.cargo }}</td>
                                          <td>{{ elm.nombre }}</td>
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
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { Caratenvue } from '@/interface/interfaces'

const cargo = ref<Array<Caratenvue>>([]);

const getCargos = () => {
axios.get('http://127.0.0.1:8000/api2/caratenvue/')
  .then(response => {
    cargo.value = response.data;
  })
  .catch(error => {
    console.error('Error Buscando Cargos:', error);
  });
};

//scrolling con teclas
const scrollTop = ref(0);

function handleKeyDown(event: { key: string; }) {
// Verificar si se presionaron las teclas de flecha
if (event.key === 'ArrowUp') {
  // Desplazar hacia arriba
  scrollTop.value -= 10; // Ajusta la cantidad de desplazamiento según sea necesario
} else if (event.key === 'ArrowDown') {
  // Desplazar hacia abajo
  scrollTop.value += 10; // Ajusta la cantidad de desplazamiento según sea necesario
}
}

onMounted(() => {
getCargos();
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