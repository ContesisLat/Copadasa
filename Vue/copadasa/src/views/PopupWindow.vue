<template>
  <div class="popup-window" v-for="(popup, index) in openedPopups" :key="index"
    :style="{ top: popup.posY + 'px', left: popup.posX + 'px', width: popup.width + 'px', height: popup.height + 'px' }"
    @mousedown="startDrag($event, index)">
    <div class="content">
      <!-- Contenido de la ventana emergente -->
      <component :is="getComponentName(index)" />
    </div>
    <button type="button" class="close-btn" aria-label="Close" @click="store.closePopup(index)">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-lg"
        viewBox="0 0 16 16">
        <path
          d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z" />
      </svg>
    </button>
    <!-- Botón para redimensionar -->
    <button class="resize-btn" @mousedown="startResize($event, index)">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-fullscreen"
        viewBox="0 0 16 16">
        <path
          d="M1.5 1a.5.5 0 0 0-.5.5v4a.5.5 0 0 1-1 0v-4A1.5 1.5 0 0 1 1.5 0h4a.5.5 0 0 1 0 1zM10 .5a.5.5 0 0 1 .5-.5h4A1.5 1.5 0 0 1 16 1.5v4a.5.5 0 0 1-1 0v-4a.5.5 0 0 0-.5-.5h-4a.5.5 0 0 1-.5-.5M.5 10a.5.5 0 0 1 .5.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 1 0 1h-4A1.5 1.5 0 0 1 0 14.5v-4a.5.5 0 0 1 .5-.5m15 0a.5.5 0 0 1 .5.5v4a1.5 1.5 0 0 1-1.5 1.5h-4a.5.5 0 0 1 0-1h4a.5.5 0 0 0 .5-.5v-4a.5.5 0 0 1 .5-.5" />
      </svg>
    </button>
  </div>
</template>

<script setup>
import { usePopupStore } from "@/store/PopupStore";
import globalComponents from "@/store/global-component";
import { ref, computed, watch } from 'vue';

const store = usePopupStore();
const openedPopups = computed(() => store.openedPopups);

// para indicar si se está redimensionando
let isResizing = false;

const startDrag = (event, index) => {
  if (!event || !event.clientX || !event.clientY || isResizing) return;
  const popup = openedPopups.value[index];
  const startX = event.clientX - popup.posX;
  const startY = event.clientY - popup.posY;

  const handleDrag = (event) => {
    if (!event.clientX || !event.clientY) return;
    popup.posX = event.clientX - startX;
    popup.posY = event.clientY - startY;
  };

  const stopDrag = () => {
    document.removeEventListener('mousemove', handleDrag);
    document.removeEventListener('mouseup', stopDrag);
  };

  document.addEventListener('mousemove', handleDrag);
  document.addEventListener('mouseup', stopDrag);
};

const startResize = (event, index) => {
  if (!event || !event.clientX || !event.clientY) return;
  const popup = openedPopups.value[index];
  let startX = event.clientX;
  let startY = event.clientY;

  // Cambiar a true durante la operación de redimensionamiento
  isResizing = true;

  const handleResize = (event) => {
    if (!event.clientX || !event.clientY) return;
    popup.width = Math.max(100, popup.width + event.clientX - startX);
    popup.height = Math.max(100, popup.height + event.clientY - startY);
    startX = event.clientX;
    startY = event.clientY;
  };

  const stopResize = () => {
    document.removeEventListener('mousemove', handleResize);
    document.removeEventListener('mouseup', stopResize);
    // Restaurar a false al finalizar la operación de redimensionamiento
    isResizing = false;
  };

  document.addEventListener('mousemove', handleResize);
  document.addEventListener('mouseup', stopResize);
};

const getComponentName = (index) => {
  const componentName = openedPopups.value[index].componentName;
  return globalComponents[componentName];
};

const centerPopup = (index) => {
  const windowWidth = window.innerWidth;
  const windowHeight = window.innerHeight;

  const popup = openedPopups.value[index];
  if (popup) {
    popup.posX = (windowWidth - popup.width) / 2;
    popup.posY = (windowHeight - popup.height) / 2;
  }
};

let previousLength = 0;

watch(() => openedPopups.value.length, (newValue) => {
  if (newValue > previousLength) {
    const lastIndex = newValue - 1; // Índice del último popup agregado
    centerPopup(lastIndex);
  }
  previousLength = newValue; // Actualizar el valor anterior
});

</script>

<style scoped>
.popup-window {
  position: absolute;
  background-color: transparent;
  border: 2px solid #ccc;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  overflow: hidden;
}

.content {
  position: relative;
  width: 100%;
  height: 100%;
}

.close-btn {
  position: absolute;
  top: 5px;
  right: 5px;
  color: black;
  border: none;
  cursor: pointer;
  background-color: transparent;
}

.resize-btn {
  position: absolute;
  bottom: 0;
  right: 0;
  padding: 5px 10px;
  background-color: darkblue;
  color: white;
  border: none;
  cursor: pointer;
}
</style>
  
  