import { defineStore } from 'pinia';

export const usePopupStore = defineStore('popup', {
  state: () => ({
    popupComponentName: "",
    openedPopups: [] as { componentName: string, width: number, height: number, posX: number, posY: number }[],
  }),
  actions: {
    openPopup(componentName: string) {
      this.openedPopups.push({
        componentName: componentName,
        width: 800, // Valor predeterminado para el ancho
        height: 500, // Valor predeterminado para el alto
        posX: 0, // Valor predeterminado para la posición X
        posY: 0, // Valor predeterminado para la posición Y
      });
      this.popupComponentName = componentName;
    },
    closePopup(index:number) {
      // Implementación del cierre de la ventana emergente
      this.openedPopups.splice(index, 1);
    },
  },
});
