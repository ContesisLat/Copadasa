<template>
    <div 
      class="popup-window" v-if="store.isPopupOpen"
      :style="{ top: posY + 'px', left: posX + 'px', width: width + 'px', height: height + 'px' }"
      @mousedown="startDrag"
    >
      <div class="content"> 
        <!-- Contenido de la ventana emergente -->
        <component :is="currentComponent"/>
      </div>
      <button type="button" class="close-btn" aria-label="Close" @click="store.closePopup"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
  <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"/>
</svg></button>
      <!-- Botón para redimensionar -->
      <button class="resize-btn" @mousedown="startResize"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-fullscreen" viewBox="0 0 16 16">
  <path d="M1.5 1a.5.5 0 0 0-.5.5v4a.5.5 0 0 1-1 0v-4A1.5 1.5 0 0 1 1.5 0h4a.5.5 0 0 1 0 1zM10 .5a.5.5 0 0 1 .5-.5h4A1.5 1.5 0 0 1 16 1.5v4a.5.5 0 0 1-1 0v-4a.5.5 0 0 0-.5-.5h-4a.5.5 0 0 1-.5-.5M.5 10a.5.5 0 0 1 .5.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 1 0 1h-4A1.5 1.5 0 0 1 0 14.5v-4a.5.5 0 0 1 .5-.5m15 0a.5.5 0 0 1 .5.5v4a1.5 1.5 0 0 1-1.5 1.5h-4a.5.5 0 0 1 0-1h4a.5.5 0 0 0 .5-.5v-4a.5.5 0 0 1 .5-.5"/>
</svg></button>
    </div>
  </template>
  
  <script lang="ts" setup>
  import {usePopupStore} from "@/store/PopupStore"
  import globalComponents from "@/store/global-component";
  import { ref,onMounted, computed } from 'vue';
  const width = ref(800);
  const height = ref(500);
  const posX = ref(0);  
  const posY = ref(0); 
  const startX = ref(0);
  const startY = ref(0);
  const isDragging = ref(false);
  const store = usePopupStore()
  const currentComponent = computed(() => {
  const componentName = store.popupComponentName;
  return globalComponents[componentName];
});


  const centerPopup = () => {
  const windowWidth = window.innerWidth;
  const windowHeight = window.innerHeight;

  posX.value = (windowWidth - width.value) / 2;
  posY.value = (windowHeight - height.value) / 2;
};

onMounted(centerPopup);
  

  const startDrag = (event: MouseEvent) => {
    if (!event.target.classList.contains('resize-btn')) {
      isDragging.value = true;
      startX.value = event.clientX - posX.value;
      startY.value = event.clientY - posY.value;
      document.addEventListener('mousemove', handleDrag);
      document.addEventListener('mouseup', stopDrag);
    }
  };
  
  const handleDrag = (event: MouseEvent) => {
    if (isDragging.value) {
      posX.value = event.clientX - startX.value;
      posY.value = event.clientY - startY.value;
    }
  };
  
  const stopDrag = () => {
    isDragging.value = false;
    document.removeEventListener('mousemove', handleDrag);
    document.removeEventListener('mouseup', stopDrag);
  };
  
  const startResize = (event: MouseEvent) => {
    let startX = event.clientX;
    let startY = event.clientY;
  
    const handleResize = (event: MouseEvent) => {
      width.value = Math.max(100, width.value + event.clientX - startX);
      height.value = Math.max(100, height.value + event.clientY - startY);
      startX = event.clientX;
      startY = event.clientY;
    };
  
    const stopResize = () => {
      document.removeEventListener('mousemove', handleResize);
      document.removeEventListener('mouseup', stopResize);
    };
  
    document.addEventListener('mousemove', handleResize);
    document.addEventListener('mouseup', stopResize);
  };
  
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
  
  