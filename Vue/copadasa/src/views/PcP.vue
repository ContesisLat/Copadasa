<template>
    <body>
    <div class="Card">
        <div class="container text-center">
        <div class="row">
            <div class="col d-flex flex-column justify-content-center align-items-center">
                <h3><strong>PAISES</strong></h3>
                <div class="card overflow-scroll" style="width:800px; height: 150px;">
                    <table class="table table-hover  table-sm">
                        <thead>
                            <tr>
                                <th>País</th>
                                <th>Nombre</th>
                                <th>Name</th>
                                <th>Iso</th>
                                <th>Phone Code</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="elm in paises" :key="elm.pais" @click="getCiudades(elm.pais)">
                                <td>{{ elm.pais }}</td>
                                <td>{{ elm.nombre }}</td>
                                <td>{{ elm.name }}</td>
                                <td>{{ elm.iso2 }}</td>
                                <td>{{ elm.phone_code }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>    
        </div>  
        <div class="row">
            <div class="col d-flex flex-column justify-content-center align-items-center">
                <h3><strong>CIUDADES</strong></h3>
                <div class="card overflow-scroll" style="width: 800px; height: 150px;">
                    <table class="table table-hover  table-sm">
                        <thead>
                            <tr>
                                <th>Ciudad</th>
                                <th>Nombre</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="elm in ciudades" :key="elm.ciudad" @click="getPuertos(elm.ciudad,elm.pais)">
                                <td>{{ elm.ciudad }}</td>
                                <td>{{ elm.nombre}}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col d-flex flex-column justify-content-center align-items-center">
                <h3><strong>PUERTOS</strong></h3>
                <div class="card overflow-scroll" style="width: 800px; height: max-content">
                    <table class="table table-hover  table-sm">
                        <thead>
                            <tr>
                                <th>Puerto</th>
                                <th>Nombre</th>
                                <th>Tipo</th>
                                <th>Pais</th>
                                <th>Ciudad</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="elm in puertos" :key="elm.puerto">
                                <td>{{ elm.puerto }}</td>
                                <td>{{ elm.nombre }}</td>
                                <td>{{ elm.tipo }}</td>
                                <td>{{ elm.nombre_pais }}</td>
                                <td>{{ elm.nombre_ciudad }}</td>
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
import { Paises,Ciudades,Puertos } from '@/interface/interfaces';

//-----------------------------------------------------------------
const paises = ref<Array<Paises>>([]);
console.log('Datos de Paises')

const getPaises = () => {
  axios.get('http://127.0.0.1:8000/api2/paises/')
    .then(response => {
      paises.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching cargos:', error);
    });
};
//----------------------------------------------------------------

const ciudades = ref<Array<Ciudades>>([])
const getCiudades = (id_pais: any) => {
     axios.get(`http://127.0.0.1:8000/api2/paises/ciudad?id_pais=${id_pais}`)
    .then(response => {
        ciudades.value = response.data;
    })
    .catch(error => {
        console.error('Error fetching ciudades:', error);
    });
  };

//----------------------------------------------------------------
const puertos = ref<Array<Puertos>>([])
const getPuertos = (id_ciudad:any,id_pais:any) => {
     axios.get(`http://127.0.0.1:8000/api2/paises/puertos?id_ciudad=${id_ciudad}&id_pais=${id_pais}`)
    .then(response => {
        puertos.value = response.data;
    })
    .catch(error => {
        console.error('Error fetching puertos:', error);
    });
  };

//-----------------------------------------------------------------
onMounted(() => {
  getPaises();
  getCiudades("1");
  getPuertos("1", "1")
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