import { createRouter,createWebHistory,RouteRecordRaw } from "vue-router";
import PageLogin from '@/components/PageLogin.vue';
import PrinPage from '@/components/PrinPage.vue';
import CarTarMan from '@/views/CarTarMan.vue';
import CarNatur from "@/views/CarNatur.vue";
import PcP from "@/views/PcP.vue";
import TarManejo from "@/views/TarManejo.vue";
import TiTarifa from "@/views/TiTarifa.vue";
import TarVue from "@/views/TarVue.vue";

const routes:Array<RouteRecordRaw> = [
    {
        path: "/",
        redirect: to => {return{name:'PageLogin'}}
    },
    {
        path:'/PageLogin',
        name:'PageLogin',
        component:PageLogin
    },
    {
        path:'/PrinPage',
        name:'PrinPage',
        component: PrinPage,
        children:[
    {
        path:'/Cartarman',
        name:'Cartarman',
        component:CarTarMan,
    },
    {
        path:'/Carnatur',
        name:'Carnatur',
        component:CarNatur
    },
    {
        path:'/PcP',
        name:'PcP',
        component:PcP
    },
    {
        path:'/TarVue',
        name:'TarVue',
        component:TarVue
    },
    {
        path:'/TarManejo',
        name:'TarManejo',
        component:TarManejo
    },
    {
        path:'/TiTarifa',
        name:'TiTarifa',
        component:TiTarifa
    },
    {
        path:'/Cargcaman',
        name:'Cargcaman',
        component:CarTarMan
    }
        ]
    },
    
    
]
const router = createRouter({
    history:createWebHistory(process.env.BASE_URL),
    routes
})

export default router