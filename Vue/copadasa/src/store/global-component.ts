import { Component } from 'vue';

import CarNatur from '@/views/CarNatur.vue';
import CargCaMan from '@/views/CargCaMan.vue';
import CarAtenVue from '@/views/CarAtenVue.vue';
import CarTarAlm from '@/views/CarTarAlm.vue';
import CarTari from '@/views/CarTari.vue';
import CarTarMan from '@/views/CarTarMan.vue';
import PcP from '@/views/PcP.vue';
import TarManejo from '@/views/TarManejo.vue';
import TarVue from '@/views/TarVue.vue';
import TiTarifa from '@/views/TiTarifa.vue';
// Importar todos los componentes globales

// objeto que contiene todos los componentes globales
const globalComponents: Record<string, Component> = {
  CarNatur,
  CargCaMan,
  CarAtenVue,
  CarTarAlm,
  CarTari,
  CarTarMan,
  PcP,
  TarManejo,
  TarVue,
  TiTarifa,
  // Agrega todos los demás componentes aquí
};

export default globalComponents;

