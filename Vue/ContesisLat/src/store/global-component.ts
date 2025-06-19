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
import LogUbica from '@/views/CargaM/LogUbica.vue';
import CarInent from '@/views/CargaM/CarInent.vue';
import CtrlManifiesto from '@/views/CargaM/CtrlManifiesto.vue';
import RegMani from '@/views/CargaM/RegMani.vue';
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
  LogUbica,
  CarInent,
  CtrlManifiesto,
  BdSeg001,
  RegMani
  // Agrega todos los demás componentes aquí
};

export default globalComponents;

