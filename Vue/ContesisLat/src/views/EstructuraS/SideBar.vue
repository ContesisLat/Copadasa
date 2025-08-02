<template>
    <a class="btn" data-bs-toggle="offcanvas" href="#offcanvasExample" role="button" aria-controls="offcanvasExample" style="color: white;">
        ☰
</a>

<div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel" style="font-family: Trebuchet MS;">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasExampleLabel">Imagen</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <div>
      <h1>texto</h1>
    </div>
    <div class="btn-group dropend">
      <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" href="#" aria-expanded="false">
        Parámetros
      </a>
      <ul class="dropdown-menu" style="cursor: pointer;">
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
        <li @click="store.openPopup('RegSerAero')"><a class="dropdown-item">Servicios Prestados</a></li>
        
        <li><a class="dropdown-item disabled" aria-disabled="true">Something else here</a></li>
        

      </ul>
    </div>
  </div>
</div>
</template>

<script lang="ts" setup>
import { usePopupStore } from '@/store/PopupStore';

const store = usePopupStore()
</script>

<style scoped>
</style>
