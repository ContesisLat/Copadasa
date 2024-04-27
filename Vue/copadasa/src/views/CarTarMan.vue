<template>
    <body>
    <div class="Card">
        <div class="container text-center">
        <div class="row">
            <div class="col d-flex flex-column justify-content-center align-items-center">
                <h3><strong>Cargos por Manejo</strong></h3>
                <div class="card overflow-scroll" style="width:800px; height: 150px;">
                    <table class="table table-hover  table-sm">
                        <thead>
                            <tr>
                                <th>Cargo</th>
                                <th>Descripción</th>
                                <th>Estado</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="elm in cargcaman" :key="elm.cargo" @click="getVigencias('01', elm.cargo)">
                                <td>{{ elm.cargo }}</td>
                                <td>{{ elm.nombre }}</td>
                                <td>{{ elm.nom_status }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>    
        </div>  
        <div class="row">
            <div class="col d-flex flex-column justify-content-center align-items-center">
                <h3><strong>Tarifas Por Cargos</strong></h3>
                <div class="card overflow-scroll" style="width: 800px; height: 150px;">
                    <table class="table table-hover  table-sm">
                        <thead>
                            <tr>
                                <th>Fecha Inicio</th>
                                <th>Fecha Final</th>
                                <th>Valor</th>
                                <th>Aplica</th>
                                <th>Estado</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="elm in cartarman" :key="elm.cargo" >
                                <td>{{ elm.fecha_inicio }}</td>
                                <td>{{ elm.fecha_final }}</td>
                                <td>{{ elm.valor }}</td>
                                <td>{{ elm.nom_aplica }}</td>
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
import { Cargcaman, Cartarman } from '@/interface/interfaces';
import { stringifyQuery } from 'vue-router';

//-----------------------------------------------------------------
const cargcaman = ref<Array<Cargcaman>>([]);
const getCargos = () => {
  axios.get(`http://127.0.0.1:8000/api2/cargcaman`)
    .then(response => {
      cargcaman.value = response.data;
      
      //console.log(cargcaman.value[0].naturaleza)
    })
    .catch(error => {
      console.error('Error al Accesar los Cargos:', error);
    });
};
//----------------------------------------------------------------
const cartarman = ref<Array<Cartarman>>([])

const getVigencias = (id_tarifa:any, id_cargo:any) => {
     axios.get(`http://127.0.0.1:8000/api2/cargcaman/cartarman?id_tarifa=${id_tarifa}&id_cargo=${id_cargo}`)
    .then(response => {
        cartarman.value = response.data;
    })
    .catch(error => {
        console.error('Error al cargar los Cargos:', error);
    });
  };
//----------------------------------------------------------------

onMounted(() => {
  getCargos();
  getVigencias("02","01")
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