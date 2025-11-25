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
                            style="background-color: transparent; border: none; outline: none; color: white;"
                            autocomplete="off" v-model="search">
                        <select
                            style="background-color: transparent; border: none; outline: none; color: black;"
                            v-model="options">
                            <option disabled value="">Select</option>
                            <option>Paises</option>
                            <option>Ciudades</option>
                            <option>Puertos</option>
                        </select>
                    </div>
                </div>
                <div class="container">
                    <div class="row">
                        <div class="col d-flex flex-column justify-content-center align-items-center">
                            <h3><strong>PAISES</strong></h3>
                            <div class="card overflow-scroll">
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
                                        <tr v-for="elm in filteredCarga1" :key="elm.pais"
                                            @click="getCiudades(elm.pais)">
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
                            <div class="card overflow-scroll">
                                <table class="table table-hover  table-sm">
                                    <thead>
                                        <tr>
                                            <th>Ciudad</th>
                                            <th>Nombre</th>
                                            <th>Pais</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="elm in filteredCarga2" :key="elm.ciudad"
                                            @click="getPuertos(elm.ciudad, elm.pais)">
                                            <td>{{ elm.ciudad }}</td>
                                            <td>{{ elm.nombre }}</td>
                                            <td>{{ elm.nombre_pais}}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col d-flex flex-column justify-content-center align-items-center">
                            <h3><strong>PUERTOS</strong></h3>
                            <div class="card overflow-scroll">
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
                                        <tr v-for="elm in filteredCarga3" :key="elm.puerto">
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
            </section>
        </div>
    </body>
</template>

<script lang="ts" setup>
import { ref, onMounted, computed,Ref } from 'vue';
import axios from 'axios';
import { Paises, Ciudades, Puertos } from '@/interface/interfaces';
import { UrlGlobal } from '@/store/dominioGlobal';

const dUrl = UrlGlobal()
const search = ref('')
const options = ref('')
//-----------------------------------------------------------------
const paises = ref<Array<Paises>>([]);

const getPaises = () => {
    axios.get(dUrl.urlGlobal +'/api2/paises/')
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
    axios.get(`${dUrl.urlGlobal}/api2/paises/ciudad?id_pais=${id_pais}`)
        .then(response => {
            ciudades.value = response.data;
        })
        .catch(error => {
            console.error('Error fetching ciudades:', error);
        });
};

//----------------------------------------------------------------
const puertos = ref<Array<Puertos>>([])
const getPuertos = (id_ciudad: any, id_pais: any) => {
    axios.get(`${dUrl.urlGlobal}/api2/paises/puertos?id_ciudad=${id_ciudad}&id_pais=${id_pais}`)
        .then(response => {
            puertos.value = response.data;
        })
        .catch(error => {
            console.error('Error fetching puertos:', error);
        });
};

//-----------------------------------------------------------------

// Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos segun la tabla------------------------------------------------
const filteredCarga1 = computed(() => {
    if (search.value === '') {
        // Si no hay nada en la búsqueda, retornar todos los registros
        return paises.value;
    } else if (options.value == 'Paises') {
        // Convertir el término de búsqueda a minúsculas para hacer la búsqueda insensible a mayúsculas
        const searchTerm = search.value.toLowerCase();
        // Filtrar los registros que coincidan con el valor de búsqueda en cualquiera de los campos
        return paises.value.filter(elm => {
            return (
                elm.pais?.toLowerCase().includes(searchTerm) ||
                elm.nombre?.toLowerCase().includes(searchTerm) ||
                elm.name?.toLowerCase().includes(searchTerm) ||
                elm.iso2?.toLowerCase().includes(searchTerm) ||
                elm.phone_code?.toLowerCase().includes(searchTerm)
            );
        });
    }else{
        return paises.value
    }
});

//----------------------------------------------------------------
const filteredCarga2 = computed(() => {
    if (search.value === '') {
        return ciudades.value;

    } else if (options.value == 'Ciudades') {
        const searchTerm = search.value.toLowerCase();

        return ciudades.value.filter(elm => {
            return (
                elm.ciudad?.toLowerCase().includes(searchTerm) ||
                elm.nombre?.toLowerCase().includes(searchTerm) 
            );
        });
    }else{
        return ciudades.value
    }
});

//----------------------------------------------------------------
const filteredCarga3 = computed(() => {
    if (search.value === '') {
        return puertos.value;
    } else if (options.value == 'Puertos') {
        const searchTerm = search.value.toLowerCase();
        return puertos.value.filter(elm => {
            return (
                elm.puerto?.toLowerCase().includes(searchTerm) ||
                elm.nombre?.toLowerCase().includes(searchTerm) ||
                elm.tipo?.toLowerCase().includes(searchTerm) ||
                elm.pais?.toLowerCase().includes(searchTerm) ||
                elm.ciudad?.toLowerCase().includes(searchTerm)
            );
        });
    }else{
        return puertos.value
    }
});
//-----------------------------------------------------------------------------------------------------------------------

onMounted(() => {
    getPaises();
    getCiudades("1");
    getPuertos("1", "1")
});
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
    @media screen and (max-width: 600px){
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
    height: 150px;
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