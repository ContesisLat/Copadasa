<template>
    <div class="modal-backdrop" v-if="props.CardReport==true" @click="handleClick"></div>
    <div class="ReportPage" v-if="props.CardReport==true">
        <h4>Correo a @ContesisLa</h4>
        <hr>
        <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Correo Electronico</label>
            <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com" style="background-color: transparent; color: white;">
        </div>
        <div class="mb-3">
            <label for="exampleFormControlTextarea1" class="form-label">Mensaje</label>
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" style="resize: vertical; background-color: transparent; color: white;"></textarea>
        </div>
        <div class="mb-3">
            <label for="formFile" class="form-label">Agregar Archivo</label>
            <input class="form-control" type="file" id="formFile" style="background-color: transparent; color: black;">
        </div>
        <hr>
        <div class="SuccessButoms"><button @click="handleClick">cancelar</button><button @click="handleClick" style="background-color:#001982">enviar</button></div>

    </div>
</template>

<script lang="ts" setup>
import { defineProps,defineEmits,Ref,ref } from 'vue'

const props = defineProps({
    CardReport: Boolean,
})
const emits = defineEmits(['updateProps'])
        const handleClick = () =>{
            emits("updateProps",!props.CardReport)
        }

</script>

<style scoped>
svg{
    fill: black;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Fondo oscuro semitransparente */
  z-index: 1050; /* Coloca el fondo oscuro por encima de otros elementos */
  
}
.ReportPage{
    min-height: 250px;
    width: 550px;
    background: whitesmoke;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 8px;
    display: flex;
    justify-content:left;
    align-items: left;
    display: flex;
    flex-direction: column;
    gap: 15px;
    font-family: Trebuchet MS;
    color: black;
    padding: 15px;
    z-index: 1060;
}
.ReportPage hr{
    border: none;
    border-top: 1px solid #ccc;
    margin:1px 0;
    padding-left: 100%;
}

.SuccessButoms{
    justify-content:right;
    align-items:right;
    flex-direction: row;
    display: flex;
    gap: 10px;
    margin-bottom: 5px;
}
.SuccessButoms button{
    border: none;
    border-radius: 4px;
    background-color: #24292F;
    color: white;
    font-family: Trebuchet MS;
    width: 90px;
    font-size: small;
    padding: 3px;
}
</style>