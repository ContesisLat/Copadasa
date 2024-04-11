<template>
    <div class="full-background">
    <DropDown/>
    <FloatingTools/>
    </div>
</template>

<script lang="ts" setup>
import DropDown from '@/views/DropDown.vue'
import FloatingTools from '@/views/FloatingTools.vue';
</script>

<style scoped>
.full-background{
    height: 100vh;
    background-color: white;
    background-image: url('@/assets/ContesisLA.png');
    background-repeat: no-repeat;
    background-size:contain;
    background-position: 50% 90px;
    position: relative;
    z-index: 1000;
}
</style>