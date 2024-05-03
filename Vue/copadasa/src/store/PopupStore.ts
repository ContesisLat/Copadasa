import { defineStore } from 'pinia';

export const usePopupStore = defineStore('popup', {
  state: () => ({
    isPopupOpen: false,
    popupComponentName: "",
  }),
  actions: {
    openPopup(componentName: string) {
      this.popupComponentName = componentName;
      this.isPopupOpen = true;
    },
    closePopup() {
      this.popupComponentName = "";
      this.isPopupOpen = false;
    },
  },
});
