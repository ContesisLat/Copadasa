<template>

    <body>
        <div class="Card">
            <section class="layout">
                <div class="header">
                </div>
                <div class="container">
                    <div class="row">
                        <div class="col d-flex flex-column justify-content-center align-items-center">
                            <h3><strong>TIPOS DE AERONAVES</strong></h3>
                            <div class="card overflow-scroll">
                                <table class="table table-hover table-sm">
                                    <thead>
                                        <tr>
                                            <th>Aeronave</th>
                                            <th>Descripcion</th>
                                            <th>Estado</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="elm in cartiaero" :key="elm.aeronave"
                                            @click="getTarifas(elm.aeronave)">
                                            <td>{{ elm.aeronave }}</td>
                                            <td>{{ elm.descripcion }}</td>
                                            <td>{{ elm.nom_status }}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col d-flex flex-column justify-content-center align-items-center">
                            <h3><strong>TARIFAS</strong></h3>
                            <div class="card overflow-scroll">
                                <table class="table table-hover table-sm">
                                    <thead>
                                        <tr>
                                            <th>Fecha Inicio</th>
                                            <th>Fecha Final</th>
                                            <th>Cargo</th>
                                            <th>Descripcion</th>
                                            <th>Costo Hora</th>
                                            <th>Estado</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="elm in cartarvue" :key="elm.aeronave">
                                            <td>{{ elm.fecha_inicio }}</td>
                                            <td>{{ elm.fecha_final }}</td>
                                            <td>{{ elm.cargo }}</td>
                                            <td>{{ elm.nombre_cargo }}</td>
                                            <td>{{ elm.costo_hora }}</td>
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
import { Cartiaero, Cartarvue } from '@/interface/interfaces';

//-----------------------------------------------------------------
const cartiaero = ref<Array<Cartiaero>>([]);
const getAeronaves = () => {
    axios.get('http://127.0.0.1:8000/api2/cartiaero/')
        .then(response => {
            cartiaero.value = response.data;
        })
        .catch(error => {
            console.error('Error al Cargar Aeronaves:', error);
        });
};
//----------------------------------------------------------------
const cartarvue = ref<Array<Cartarvue>>([])
const getTarifas = (id_aeronave: any) => {
    axios.get(`http://127.0.0.1:8000/api2/cartiaero/cartarvue?id_aeronave=${id_aeronave}`)
        .then(response => {
            cartarvue.value = response.data;
        })
        .catch(error => {
            console.error('Error al cargar los Cargos:', error);
        });
};

//----------------------------------------------------------------

onMounted(() => {
    getAeronaves();
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
    height: 150px;
    min-width: min-content;
    min-height: min-content;
    box-sizing: border-box;
}
</style>