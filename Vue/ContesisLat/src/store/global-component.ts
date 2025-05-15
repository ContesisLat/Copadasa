import { Component } from 'vue';

import CarNatur from '@/views/CargaM/CarNatur.vue';
import CargCaMan from '@/views/CargaM/CargCaMan.vue';
import CarAtenVue from '@/views/CargaM/CarAtenVue.vue';
import CarTarAlm from '@/views/CargaM/CarTarAlm.vue';
import CarTari from '@/views/CargaM/CarTari.vue';
import CarTarMan from '@/views/CargaM/CarTarMan.vue';
import PcP from '@/views/CargaM/PcP.vue';
import TarManejo from '@/views/CargaM/TarManejo.vue';
import TarVue from '@/views/CargaM/TarVue.vue';
import TiTarifa from '@/views/CargaM/TiTarifa.vue';
import BdSeg001 from '@/views/SeguridadM/BdSeg001.vue';
import ImpresorasSeg003 from '@/views/SeguridadM/ImpresorasSeg003.vue';
import AxCSeg002 from '@/views/SeguridadM/AxCSeg002.vue';
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
  BdSeg001
  // Agrega todos los demás componentes aquí
};

export default globalComponents;

