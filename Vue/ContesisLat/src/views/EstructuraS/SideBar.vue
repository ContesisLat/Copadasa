<template>
<<<<<<< HEAD
  <!-- Botón para abrir el menú -->
  <a class="btn" @click="cargarProgramas(perfil)" data-bs-toggle="offcanvas" href="#offcanvasExample" role="button"
    aria-controls="offcanvasExample" style="color: white; border: none; border-radius: 5px;">
    ☰
  </a>

  <!-- Panel lateral -->
  <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">

=======
  <a class="btn" data-bs-toggle="offcanvas" href="#offcanvasExample" role="button" aria-controls="offcanvasExample"
    style="color: white;">
    ☰
  </a>

  <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel"
    style="font-family: Trebuchet MS;">
>>>>>>> 25c1d2ded1cd92aad99f2bf0cb6f741a09d0a518
    <div class="offcanvas-header">
      <h3>Estrategia Cargo</h3>
      <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>
    <div class="offcanvas-body d-flex flex-column gap-2">
<<<<<<< HEAD

      <!-- Iteramos sobre los programas -->
      <div class="btn-group dropend" v-for="(programa, index) in programas" :key="index">

        <!-- Nombre del programa -->
=======
      <div>
        <h1>texto</h1>
      </div>
      <div class="btn-group dropend">
>>>>>>> 25c1d2ded1cd92aad99f2bf0cb6f741a09d0a518
        <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" href="#" aria-expanded="false">
          Parámetros
        </a>
        <ul class="dropdown-menu" style="cursor: pointer;">
<<<<<<< HEAD
          <div class="dropdown-inner">

            <li v-for="(sub, i) in programa.subprogramas" :key="i" @click="store.openPopup(sub.programa)">
              <a class="dropdown-item">{{ sub.descripcion }}</a>
            </li>

            <!-- Si no tiene subprogramas -->
            <li v-if="programa.subprogramas.length === 0">
              <a class="dropdown-item disabled" aria-disabled="true">
                Sin subprogramas
              </a>
            </li>

          </div>
=======
          <li @click="store.openPopup('PcP')"><a class="dropdown-item">Países/Ciudades/Puertos</a></li>
          <li @click="store.openPopup('CrmClte')"><a class="dropdown-item">Catálogo de Clientes</a></li>
          <li @click="store.openPopup('CarNatur')"><a class="dropdown-item">Naturaleza de Carga</a></li><br>
          <li @click="store.openPopup('TiTarifa')"><a class="dropdown-item">Definición de Tarifas</a></li>
          <li @click="store.openPopup('CarTarMan')"><a class="dropdown-item">Tarifas por Manejo</a></li>
          <li @click="store.openPopup('CarTarAlm')"><a class="dropdown-item">Tarifas por Almacenaje</a></li>
          <li @click="store.openPopup('CarTari')"><a class="dropdown-item">Tarifas Refrigeración</a></li><br>

          <li @click="store.openPopup('CarAtenVue')"><a class="dropdown-item">Cargos por Atención de Vuelos</a></li>
          <li @click="store.openPopup('TarVue')"><a class="dropdown-item">Tarifa Atención de Vuelos</a></li>
          <li @click="store.openPopup('CarCoaer')"><a class="dropdown-item">Compañías Aéreas</a></li><br>

          <li @click="store.openPopup('LogAlma')"><a class="dropdown-item">Definición de Almacenes</a></li>
          <li @click="store.openPopup('LogTral')"><a class="dropdown-item">Transacciones de Almaén</a></li>
          <li @click="store.openPopup('CarInent')"><a class="dropdown-item">Indicadores de Entrega</a></li>
          <li @click="store.openPopup('LogUbica')"><a class="dropdown-item">Ubicaciones en Almacén</a></li>

          <li @click="store.openPopup('BdSeg001')"><a class="dropdown-item">bases de datos</a></li>

          <li><a class="dropdown-item disabled" aria-disabled="true">Something else here</a></li>
        </ul>
      </div>
      <div class="btn-group dropend">
        <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" href="#" aria-expanded="false">
          Manifiestos

        </a>
        <ul class="dropdown-menu" style="cursor: pointer;">
          <li @click="store.openPopup('RegMani')"><a class="dropdown-item">Registro Manifiestos</a></li>
          <li @click="store.openPopup('CtrlManifiesto')"><a class="dropdown-item">Control de Manifiestos</a></li>
          <li @click="store.openPopup('CtrlDespacho')"><a class="dropdown-item">Despachos</a></li>


          <li><a class="dropdown-item disabled" aria-disabled="true">Something else here</a></li>
        </ul>
      </div>
      <div class="btn-group dropend">
        <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" href="#" aria-expanded="false">
          Aeronaves

        </a>
        <ul class="dropdown-menu" style="cursor: pointer;">
          <li @click="store.openPopup('RegSerAero')"><a class="dropdown-item">Servicios a Aeronaves</a></li>

          <li><a class="dropdown-item disabled" aria-disabled="true">Something else here</a></li>
        </ul>
      </div>
      <div class="btn-group dropend">
        <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" href="#" aria-expanded="false">
          Almacén Frío

        </a>
        <ul class="dropdown-menu" style="cursor: pointer;">
          <li @click="store.openPopup('CtrlCuartofrio')"><a class="dropdown-item">Control Cuarto Frío</a></li>

          <li><a class="dropdown-item disabled" aria-disabled="true">Something else here</a></li>
        </ul>
      </div>
      <div class="btn-group dropend">
        <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" href="#" aria-expanded="false">
          Consulta/Reportes

        </a>
        <ul class="dropdown-menu" style="cursor: pointer;">
          <li @click="store.openPopup('ExResSerAero')"><a class="dropdown-item">Servicios Aéreos</a></li>

          <li><a class="dropdown-item disabled" aria-disabled="true">Something else here</a></li>


>>>>>>> 25c1d2ded1cd92aad99f2bf0cb6f741a09d0a518
        </ul>

      </div>

    </div>
  </div>
</template>

<<<<<<< HEAD


=======
>>>>>>> 25c1d2ded1cd92aad99f2bf0cb6f741a09d0a518
<script lang="ts" setup>
import { usePopupStore } from '@/store/PopupStore';

const store = usePopupStore()
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

body {
  font-family: 'Poppins', sans-serif;
}



.btn {
  background-color: #001982;
  padding: 4px 9px;
  font-size: 15px;
  transition: transform 0.2s ease;
}

.btn:focus {
  background-color: #001982;

}

.btn:active {
  transform: scale(0.95);
}

/* Asegura que el menú esté disponible para animar */
.dropdown-menu {
  display: block !important;
  padding: 8px;
  background: transparent;
  border: none;
  visibility: hidden;
  pointer-events: none;
}

/* Contenedor interno animado */
.dropdown-inner {
  background: rgba(255,255,255,0.95); 
  border-radius: 12px;
  padding: 8px;
  box-shadow: 0 18px 40px rgba(6, 18, 50, 0.22);
  transform-origin: 0 0;
  transform: scale(0.96) translateX(-6px);
  opacity: 0;
  transition: transform 0.33s cubic-bezier(.22,.9,.3,1), 
              opacity 0.33s ease, 
              box-shadow 0.33s ease;
  backdrop-filter: blur(6px);
}

/* Cuando el menú se abre */
.show.dropdown-menu {
  visibility: visible;
  pointer-events: auto;
}

.show.dropdown-menu .dropdown-inner {
  transform: scale(1) translateX(0);
  opacity: 1;
}


/* ===========================================
   ANIMACIÓN PREMIUM PARA EL SIDEBAR (OFFCANVAS)
=========================================== */

/* Estado inicial (oculto) */
.offcanvas {
  transform: translateX(-30px);      /* No tan lejos → más fluido */
  opacity: 0;                        /* Se desvanece en vez de aparecer de golpe */
  transition:
    transform 0.30s cubic-bezier(.25,.8,.25,1),
    opacity 0.25s ease;
  will-change: transform, opacity;
  box-shadow: none !important;
  
}

/* Cuando está visible (Bootstrap agrega .show) */
.offcanvas.show {
  transform: translateX(0);          /* Entra suave */
  opacity: 1;                        /* Se desvanece */
  box-shadow: 8px 0 35px rgba(0,0,0,0.25) !important;
}

/* Cerrar con animación también (Bootstrap quita .show,
   pero TRABAJA el frame antes de ocultarlo completamente) */
.offcanvas.hiding {
  transform: translateX(-20px);      /* Se va un poco hacia atrás */
  opacity: 0;                        /* Se desvanece */
  transition:
    transform 0.35s cubic-bezier(.4,0,.2,1),
    opacity 0.3s ease;
}

/* Contenido interno con "delay suave" */
.offcanvas-body {
  opacity: 0;
  transform: translateX(-10px) scale(0.98);
  transition:
    opacity 0.35s ease,
    transform 0.4s cubic-bezier(.25,.9,.3,1);
  will-change: opacity, transform;
}

/* Cuando el panel está abierto*/
.offcanvas.show .offcanvas-body {
  opacity: 1;
  transform: translateX(0) scale(1);
}


</style>
