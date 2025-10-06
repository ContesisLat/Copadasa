<template>

    <button type="button" class="btn btn-light" @click="generarPDF">
        Generar PDF
    </button>

</template>

<script lang="ts" setup>
import { defineProps,defineEmits,Ref,ref } from "vue"
import axios from "axios"
import { useDateTimeStore } from '@/store/dateTimeStore';
import { userGlobalStore } from '@/store/userGlobal';
import { UrlGlobal } from '@/store/dominioGlobal';

const dUrl = UrlGlobal()
const dateTimeStore = useDateTimeStore();
const userStore = userGlobalStore();

const props = defineProps({
    numV: String,
    fechaM:String,
    piezas:String,
    peso:String,
    numEm:String,
    destinatario:String,
    liquidaA:String,
})

const generarPDF = async () => {
    try {
        const payload = {
            numero_vuelo: props.numV,
            fecha_manifiesto: props.fechaM,
            pieza_entrega: props.piezas,
            peso: props.peso,
            no_embarque:props.numEm,
            destinatario: props.destinatario,
            liquida_aduana: props.liquidaA,
            fecha_entrega: dateTimeStore.formattedDate,
            hecho_por: userStore.globalUser,
        }

        const response = await axios.post(
            dUrl.urlGlobal + "/api2/informe-entrega",
            payload,
            { responseType: "blob" } // importante para PDF
        )

        // Crear descarga del PDF
        const blob = new Blob([response.data], { type: "application/pdf" })
        const link = document.createElement("a")
        link.href = URL.createObjectURL(blob)
        link.download = "informe_entrega.pdf"
        link.click()
    } catch (error) {
        console.error("Error generando PDF:", error)
    }
}
</script>

<style scoped>
button{
    transition: transform 0.2s ease;
}
button:active{
    transform: scale(0.95);
}
</style>