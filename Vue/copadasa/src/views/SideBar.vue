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
        Programas Prueba
      </a>
      <ul class="dropdown-menu" >
        <li><router-link to="/CargCaMan" class="dropdown-item">Carga por manejo</router-link></li>
        <li><router-link to="/CarNatur" class="dropdown-item">Naturaleza</router-link></li>
        <li><router-link to="/PcP" class="dropdown-item">PcP</router-link></li>
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
