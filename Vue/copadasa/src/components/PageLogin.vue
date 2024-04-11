<template>
    <div id="app2">
     <div class="form">
       <h4 style="font-family:Lucida Handwriting,cursive"><b>Login</b></h4>
       <h2><b>Contesis <br>Latinoamerica</b></h2><br>
 
        <div class="inputbox">
         <input v-model="username" type="text" required id="User">
         <label for="email"><b>Usuario</b></label>
         <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person" viewBox="0 0 16 16">
            <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6m2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0m4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4m-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664z"/>
         </svg> 
        </div>
 
        <div class="inputbox">
           <input v-model="password" type="password" required id="password" >
           <label for="password"><B>Password</B></label>
           <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lock" viewBox="0 0 16 16">
             <path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2zM5 8h6a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/>
           </svg>
           
         </div>
         <button @click.prevent="validation">Log in</button>
        
 
        
     </div>
    </div>
 </template>
 
 <script lang="ts" setup>
import { onMounted, ref } from 'vue';
import LoginService from '@/services/LoginService';
import { useRouter } from 'vue-router';

const username = ref<string>('');
const password = ref<string>('');
const router = useRouter();

const validation = async (): Promise<void> => {
    try {
        const credential = new LoginService();
        // Espera a que la solicitud se complete y actualice la variable 'user'
        await credential.fetchByLogin(username.value, password.value);

        // Obtén el usuario después de que la solicitud se complete
        const user = credential.getMs();

        console.log(user.value)

        // Validación
        if (!!user.value && user.value.message === 'Autenticacion exitosa') {
            router.push('/PrinPage');
            console.log('Credenciales válidas');
        } else {
            console.log('Credenciales inválidas');
        }
    } catch (error) {
        console.error('Error al realizar la validación:', error);
    }
};

onMounted(() => {
    //por si quiero poner algo antes cuando se monta la pagina
});
    
 </script>
 
 <style scoped>
 #app2{
   position: absolute;
   top: 50%;
   left: 50%;
   transform: translate(-50%, -50%);
 }
 
 .form{
     position: relative;
     width: 400px;
     height: 450px;
     background:transparent;
     box-shadow: 0 0 5px gray, 0 0 25px
     gray,0 0 50px gray,0 0 200px gray;
     border-radius: 20px;
     display: flex;
     justify-content: center;
     align-items: center;
     display: flex;
     flex-direction: column;
     backdrop-filter: blur(10px);
     color:black;
     font-family: Trebuchet MS;
 
 }
 .inputbox{
   display: flex;
   align-items: center;
   width: 80%;
 }
 .inputbox input{
   width: 100%;
   height: 50px;
   background: transparent;
   margin-bottom: 2em;
   padding: 1em 0 0 0.5em;
   border: none;
   border-bottom: 1px solid black;
   font-size: small;
   outline: none;
   color: black;
   padding-right: 20px;
 }
  .inputbox svg{
   transform: translateY(-50%) translateX(-90%);
   fill:black/*para cambiar el color del contenido */
  }
  .inputbox label{
   position: absolute;
   left: 12%;
   transform: translateY(-50%);
   transition: transform 200ms;
   pointer-events: none/* evita q el label interfiera en el input*/;
  }
   input:focus + label,
   input:valid + label{
   transform: translate(0,-30px) scale(0.8);
  }
  h2{
   position: absolute;
   text-align: center;
   top: 14%;
   text-shadow: 0 0 5px white;
  }
  h4{
    position: absolute;
    top: 5%;
    left: 5%;
    color: darkblue;
  }
 
  button{
   width: 80%;
   min-width: 250px;
   border-radius: 20px;
   background-color: darkblue;
   box-shadow: 0 1em 4em rgba(212, 234, 255, 0.2);
   border: none;
   color: white;
  }
 
 </style>