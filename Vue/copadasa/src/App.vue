<template>
  <router-view/>
</template>

<script lang="ts" setup>
import PageLogin from './components/PageLogin.vue';
</script>

<style>
#app {
  height: 80vh;
  background: white;
  background-image: url('@/assets/ContesisLA.png');
  background-repeat: no-repeat;
  background-size:contain;
  background-position: 50% 30px;
}
</style>
