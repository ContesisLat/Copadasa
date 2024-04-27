<template>
<body>
    <div class="Card">
      <div class="container text-center">
      <div class="row">
        <div class="col d-flex flex-column justify-content-center align-items-center">
          <h3><strong>Naturaleza</strong></h3>
          <div class="card overflow-scroll" style="width: max-content; height: 50%;">
            <table class="table table-hover table-sm">
              <thead>
                <tr>
                    <th>Naturaleza</th>
                    <th>Nombre</th>
                    <th>Cargo</th>
                    <th>Descripcion</th>
                    <th>Status</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="elm in carga" :key="elm.naturaleza">
                    <td>{{ elm.naturaleza }}</td>
                    <td>{{ elm.nombre }}</td>
                    <td>{{ elm.cargo }}</td>
                    <td>{{ elm.nom_cargo }}</td>
                    <td>{{ elm.nom_status }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      </div>
    </div>
</body>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import {Natur} from '@/interface/interfaces'

const carga = ref<Array<Natur>>([]);

const getCarga = () => {
  axios.get('http://127.0.0.1:8000/api2/carnatur/')
    .then(response => {
      carga.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching cargos:', error);
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
  getCarga();
});
</script>

<style scoped>
body{
    height: 100%;
    width: 100%;
    background: transparent;
    backdrop-filter: blur(10px);
}
.Card{
   position: relative;
   top: 50%;
   left: 50%;
   transform: translate(-50%, -50%);
   width: 80%;
   height: 75%;
   display: flex;
   border-radius: 10px;
   justify-content: center;
   align-items: center;
   flex-direction: column;
   text-align: center;
   font-family: Trebuchet MS;
   color: white;
   background: linear-gradient(to right,#ccd0cf,#9ba8ab,#4a5c6a);
   overflow: hidden;
}

  
</style>