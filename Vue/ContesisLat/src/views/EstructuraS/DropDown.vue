<template>
    <div class="background">
        <nav class="menu-wrapper">
            <div class="menu-bar">
                <SideBar/>
                <ul class="navigation hide">
                    <li>
                        <button>Compañia</button>
                        <div class="dropdown">
                            <h3>for</h3>
                            <ul class="list-menu-items">
                                <li>
                                    <a href="#" title="enterprise">info</a>
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li>
                        <button>Agencia</button>
                        <div class="dropdown">
                            <h3>for</h3>
                            <ul class="list-menu-items">
                                <li>
                                    <a href="#" title="enterprise">info</a>
                                </li>
                            </ul>
                        </div>
                    </li>
                </ul>

            </div>
            <div class="action-buttons">
                <router-link to="/"><a href="#" title="sign out" class="secondary hide" style="font-family:Lucida Handwriting,cursive">{{ gUser.globalUser }}</a></router-link>
                <span class="dateTime"> 
                    <p>{{ currentDate }}</p>
                    <p>{{ currentTime }}</p>
                </span>
                
            </div>
            

        </nav>
    </div>
</template>

<script lang="ts" setup>
import SideBar from '@/views/EstructuraS/SideBar.vue'
import{ref,onMounted} from "vue"
import { userGlobalStore } from '@/store/userGlobal';

let gUser = userGlobalStore()
    const currentDate=ref('')
    const currentTime=ref('')
    
    const updateTime=()=>{
        const now = new Date();
        currentDate.value=formatDate(now);
        currentTime.value=formatTime(now);
    }

    const formatDate=(date: Date)=>{
        const year= date.getFullYear();
        const month = (date.getMonth() + 1).toString().padStart(2, '0');
        const day = date.getDate().toString().padStart(2, '0');
        return `${day}/${month}/${year}`;
    }

    const formatTime=(date:Date)=>{
        const hours = date.getHours().toString().padStart(2 , '0');
        const minutes = date.getMinutes().toString().padStart(2, '0');
        const seconds = date.getSeconds().toString().padStart(2, '0');
        return `${hours}:${minutes}:${seconds}`;
    }

    onMounted(() => {
        updateTime();
        setInterval(updateTime,1000)
    })

</script>

<style scoped>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.menu-wrapper{
    display: flex;
    position: fixed;
    flex-direction: row;
    justify-content: space-between;
    width: 100vw;
    z-index: 2;
    gap: 24px;
    background-color: #24292F;
    height: 60px;
    padding: 0px 16px;
    align-items: center;
}
.menu-bar{
    display: flex;
    gap: 24px;
    align-items: center;
    @media screen and (max-width:600px){
        gap: 10px;
    }
}
.logo{
    width: 32px;
    height: 32px;
    cursor: pointer;
}
.logo svg{
    fill: white;
}
.navigation{
    display: flex;
    flex-direction: row;
    list-style-type: none;
    align-items: center;
    gap:8px;
    background-color: #24292F;
    font-family: Trebuchet MS;
}
.navigation > li{
    display: flex;
    position: relative;
    cursor: pointer;
    align-items: center;
    height: 42px;
}
.navigation > li > button > svg{
    stroke: white;
    fill: white;
    color: white;
    margin-top: -2px;
    transition: all 0.2s ease-in-out;
}
.navigation > li > a{
    color: white;
    font-size: 14px;
    text-decoration: none;
}
.navigation > li > button{
    color: white;
    border-bottom: 2px solid transparent;
    transition: all 0.3 ease;
    text-decoration: none;
    border: none;
    cursor: pointer;
    font-weight: 500;
    gap: 4px;
    opacity: 1;
    align-items: center;
    font-size: 14px;
    flex-wrap: nowrap;
    white-space: nowrap;
    background: none;
    display: flex;
    padding: 3px 0;
    position: relative;
    transition: all 0.2s ease-in-out;
}
.navigation > li > button:hover,
.navigation > li > a:hover{
    opacity: 0.75;
}
.navigation > li > button:hover > svg{
    opacity: 0.75;
    margin-top: 6px;
}
.dropdown{
    position: absolute;
    top: 42px;
    min-width: 240px;
    border-radius: 8px;
    background-color: white;
    color: black;
    display: none;
    flex-direction: column;
    padding: 16px;
    box-shadow: 0 0 5px gray, 0 0 10px
     gray,0 0 25px gray,0 0 100px gray;
    z-index: 2;
    animation: fadeIn 0.2s ease-in-out;
}
@keyframes fadeIn{
    from{
        opacity: 0;
        transform: scale(0.99) translateY(-0.7em);
        transform-origin: top;
    }
    to{
        opacity: 1;
        transform: scale(1) translateY(0);
    }
}
.dropdown h3 {
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 8px;
}
.list-menu-items{
    display: flex;
    list-style-type: none;
    flex-direction: column;
    gap:4px;
}
.list-menu-items > li > a{
    display: flex;
    gap: 16px;
    font-size: 14px;
    width: 100%;
    color: #847f90;
    text-decoration: none;
}
.list-menu-items > li > a:hover{
    color: #0969DA;
}
.list-items-with-description{
    list-style-type: none;
}
.list-items-with-description li{
    display: flex;
    padding: 4px;
    gap: 16px;
    width: 100%;
}
.list-items-with-description li:hover{
    color:#0969DA;
}
.list-items-with-description li svg{
    margin-top: 4px;
    width: 16px;
    height: 16px;
}
.list-items-with-description li:hover svg{
    stroke:#0969DA;
}
.item-title h3{
    font-size: 14px;
    font-weight: 600;
}
.item-title p{
    font-size: 12px;
}
.navigation > li:hover .dropdown{
    display: flex;
    opacity: 1;
}
.action-buttons{
    display: flex;
    gap: 8px;
    align-items: center;
    flex-wrap: nowrap;
    @media  screen and (max-width:600px) {
        gap: 3px;
    }
}
.action-buttons a{
    text-decoration: none;
    font-size: 16px;
    white-space:nowrap;
    padding: 4px 8px;
    transition: all 0.2s ease-in-out;
}
.action-buttons a:hover{
    opacity: .75;
}
.secondary{
    background: none;
    color: white;
    outline: none;
    border: none;
}

.dateTime{
    flex-direction: column;
    font-family:Trebuchet MS ;
    display: flex;
    justify-content: center;
    align-items: center;
}
.dateTime p{
    height: 15px;
    font-size: small;
    color: white;

}

</style>