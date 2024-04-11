<template>
<body>
    <div class="Card">
      <div class="container text-center">
      <div class="row">
        <div class="col d-flex flex-column justify-content-center align-items-center">
          <h3><strong>Cargo Por Manejo</strong></h3>
          <div class="card overflow-scroll" style="width: max-content; height: 72%;">
            <table class="table table-hover table-striped table-sm">
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
   width: 70%;
   height: 70%;
   display: flex;
   border-radius: 10px;
   justify-content: center;
   align-items: center;
   flex-direction: column;
   text-align: center;
   font-family:Trebuchet MS;
   overflow-y: auto;
   color: white; 
   background: #24292F;
   /*background: rgb(189, 189, 189);
    background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(255,143,38,1) 0%, rgba(150,126,197,1) 48%, rgba(0,255,222,1) 100%);
    background-size: 300% 100%;
    animation: gradient 15s ease infinite;*/  
}

/*  @keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
} */

</style>