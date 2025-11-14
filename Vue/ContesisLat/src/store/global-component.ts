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
import CarCoaer from '@/views/CargaM/CarCoaer.vue';
import CtrlManifiesto from '@/views/CargaM/CtrlManifiesto.vue';
import RegMani from '@/views/CargaM/RegMani.vue';
import RegSerAero from '@/views/CargaM/RegSerAero.vue';
import LogTral from '@/views/CargaM/LogTral.vue';
import CtrlDespacho from '@/views/CargaM/CtrlDespacho.vue';
import CtrlCuartofrio from '@/views/CargaM/CtrlCuartofrio.vue';
import CrmClte from '@/views/CargaM/CrmClte.vue';
import LogAlma from '@/views/CargaM/LogAlma.vue';
import ExResSerAero from '@/views/CargaM/pImpresion/ExResSerAero.vue';

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
  CarCoaer,
  LogTral,
  CtrlManifiesto,
  BdSeg001,
  RegMani,
  RegSerAero,
  CtrlDespacho,
  CtrlCuartofrio,
  CrmClte,
  LogAlma,
  ExResSerAero
  // Agrega todos los demás componentes aquí
};

export default globalComponents;

