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
      <ul class="dropdown-menu" >
        <li><router-link to="/PcP" class="dropdown-item">Países/Ciudades/Puertos</router-link></li>
        <li><router-link to="/CarNatur" class="dropdown-item">Naturaleza de Carga</router-link></li><br>
        <li><router-link to="/TiTarifa" class="dropdown-item">Definición de Tarifas</router-link></li>
        <li><router-link to="/CarTarMan" class="dropdown-item">Tarifas por Manejo</router-link></li>
        <li><router-link to="/TarMan" class="dropdown-item">Tarifas por Almacenaje</router-link></li>
        <li><router-link to="/TarRef" class="dropdown-item">Tarifas Cuarto Frío</router-link></li>

        <li><router-link to="/TarVue" class="dropdown-item">Tarifa Atención de Vuelos</router-link></li>
        <li><a class="dropdown-item disabled" aria-disabled="true">Something else here</a></li>
      </ul>
    </div>
  </div>
</div>
</template>

<script lang="ts" setup>
</script>

<style scoped>
</style>
