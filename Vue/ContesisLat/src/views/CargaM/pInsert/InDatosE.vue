<template>
    <div class="modal-backdrop"></div>
    <div class="ReportPage">
        <section class="layout">
            <div class="header">
                <h4>Datos de Entrega</h4>
                <button @click="handleClick">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                        class="bi bi-x-lg" viewBox="0 0 16 16">
                        <path
                            d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z" />
                    </svg>
                </button>
            </div>
            <div class="container">
                <div class="d-flex flex-column justify-content-center align-items-center w-100" style="height: 100%;">
                    <div id="carouselExampleIndicators" ref="carouselRef" class="carousel carousel-dark slide w-100"
                        data-bs-interval="false" style="height: 100%; position: relative;">
                        <div class="carousel-indicators">
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0"
                                class="active" aria-current="true" aria-label="Slide 1"></button>
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
                                aria-label="Slide 2"></button>
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"
                                aria-label="Slide 3"></button>
                        </div>
                        <div class="carousel-inner w-100 h-100">
                            <!-- Slide para Matrícula -->
                            <div class="carousel-item active h-100">
                                <div class="d-flex justify-content-center align-items-center h-100">
                                    <div class="row">
                                        <div class="col-auto text-center">
                                            <div class="devices">
                                                <div>
                                                    <video v-if="isCameraActive1" ref="video1" autoplay
                                                        class="media-box"></video>
                                                    <img v-if="photo1" :src="photo1" alt="Foto matrícula"
                                                        class="media-box" />
                                                    <canvas ref="canvas1" class="media-box"
                                                        style="display: none;"></canvas>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-auto text-center">
                                            <h5><strong>Matrícula</strong></h5>
                                            <div class="btn-group">
                                                <button @click="startCamera(1)">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                        fill="currentColor" class="bi bi-camera" viewBox="0 0 16 16">
                                                        <path
                                                            d="M15 12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1.172a3 3 0 0 0 2.12-.879l.83-.828A1 1 0 0 1 6.827 3h2.344a1 1 0 0 1 .707.293l.828.828A3 3 0 0 0 12.828 5H14a1 1 0 0 1 1 1zM2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4z" />
                                                        <path
                                                            d="M8 11a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5m0 1a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7M3 6.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0" />
                                                    </svg>
                                                </button>
                                                <button @click="changeCamera(1)">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                        fill="currentColor" class="bi bi-arrow-repeat"
                                                        viewBox="0 0 16 16">
                                                        <path
                                                            d="M11.534 7h3.932a.25.25 0 0 1 .192.41l-1.966 2.36a.25.25 0 0 1-.384 0l-1.966-2.36a.25.25 0 0 1 .192-.41m-11 2h3.932a.25.25 0 0 0 .192-.41L2.692 6.23a.25.25 0 0 0-.384 0L.342 8.59A.25.25 0 0 0 .534 9" />
                                                        <path fill-rule="evenodd"
                                                            d="M8 3c-1.552 0-2.94.707-3.857 1.818a.5.5 0 1 1-.771-.636A6.002 6.002 0 0 1 13.917 7H12.9A5 5 0 0 0 8 3M3.1 9a5.002 5.002 0 0 0 8.757 2.182.5.5 0 1 1 .771.636A6.002 6.002 0 0 1 2.083 9z" />
                                                    </svg>
                                                </button>
                                                <button @click="takePicture(1)">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                        fill="currentColor" class="bi bi-circle" viewBox="0 0 16 16">
                                                        <path
                                                            d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16" />
                                                    </svg>
                                                </button>
                                                <button @click="removePhoto(1)">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                        fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                                        <path
                                                            d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z" />
                                                        <path
                                                            d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2(Base64)h-11z" />
                                                    </svg>
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- Slide para Cédula -->
                            <div class="carousel-item h-100">
                                <div class="d-flex justify-content-center align-items-center h-100">
                                    <div class="row">
                                        <div class="col-auto text-center">
                                            <div class="devices">
                                                <div>
                                                    <video v-if="isCameraActive2" ref="video2" autoplay
                                                        class="media-box"></video>
                                                    <img v-if="photo2" :src="photo2" alt="Foto cédula"
                                                        class="media-box" />
                                                    <canvas ref="canvas2" class="media-box"
                                                        style="display: none;"></canvas>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-auto text-center">
                                            <h5><strong>Cédula</strong></h5>
                                            <div class="btn-group">
                                                <button @click="startCamera(2)">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                        fill="currentColor" class="bi bi-camera" viewBox="0 0 16 16">
                                                        <path
                                                            d="M15 12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1.172a3 3 0 0 0 2.12-.879l.83-.828A1 1 0 0 1 6.827 3h2.344a1 1 0 0 1 .707.293l.828.828A3 3 0 0 0 12.828 5H14a1 1 0 0 1 1 1zM2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4z" />
                                                        <path
                                                            d="M8 11a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5m0 1a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7M3 6.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0" />
                                                    </svg>
                                                </button>
                                                <button @click="changeCamera(2)">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                        fill="currentColor" class="bi bi-arrow-repeat"
                                                        viewBox="0 0 16 16">
                                                        <path
                                                            d="M11.534 7h3.932a.25.25 0 0 1 .192.41l-1.966 2.36a.25.25 0 0 1-.384 0l-1.966-2.36a.25.25 0 0 1 .192-.41m-11 2h3.932a.25.25 0 0 0 .192-.41L2.692 6.23a.25.25 0 0 0-.384 0L.342 8.59A.25.25 0 0 0 .534 9" />
                                                        <path fill-rule="evenodd"
                                                            d="M8 3c-1.552 0-2.94.707-3.857 1.818a.5.5 0 1 1-.771-.636A6.002 6.002 0 0 1 13.917 7H12.9A5 5 0 0 0 8 3M3.1 9a5.002 5.002 0 0 0 8.757 2.182.5.5 0 1 1 .771.636A6.002 6.002 0 0 1 2.083 9z" />
                                                    </svg>
                                                </button>
                                                <button @click="takePicture(2)">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                        fill="currentColor" class="bi bi-circle" viewBox="0 0 16 16">
                                                        <path
                                                            d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16" />
                                                    </svg>
                                                </button>
                                                <button @click="removePhoto(2)">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                        fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                                        <path
                                                            d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z" />
                                                        <path
                                                            d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z" />
                                                    </svg>
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- Slide para Firma -->
                            <div class="carousel-item h-100">
                                <div class="d-flex justify-content-center align-items-center h-100">
                                    <div class="row">
                                        <div class="col-auto text-center">
                                            <div class="border border-black-500" style="height: 250px; width:500px;">
                                                <canvas class="canvasFirm" ref="canvasRef"></canvas>
                                            </div>
                                        </div>
                                        <div class="col-auto text-center">
                                            <h5><strong>Firma</strong></h5>
                                            <div class="btn-group">
                                                <button @click="enviarDatos">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                        fill="currentColor" class="bi bi-check2-circle"
                                                        viewBox="0 0 16 16">
                                                        <path
                                                            d="M2.5 8a5.5 5.5 0 0 1 8.25-4.764.5.5 0 0 0 .5-.866A6.5 6.5 0 1 0 14.5 8a.5.5 0 0 0-1 0 5.5 5.5 0 1 1-11 0" />
                                                        <path
                                                            d="M15.354 3.354a.5.5 0 0 0-.708-.708L8 9.293 5.354 6.646a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0z" />
                                                    </svg>
                                                </button>
                                                <button @click="limpiarFirma">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                        fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                                        <path
                                                            d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z" />
                                                        <path
                                                            d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z" />
                                                    </svg>
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <button class="carousel-control-prev custom-control" type="button"
                            data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                        </button>
                        <button class="carousel-control-next custom-control" type="button"
                            data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                        </button>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, onUnmounted, defineProps, defineEmits } from 'vue';
import { Carousel } from 'bootstrap';
import SignaturePad from 'signature_pad';
import { useAlert } from '@/store/useAlert';
const { success, error, question, warning } = useAlert()
import { UrlGlobal } from '@/store/dominioGlobal';
import { userGlobalStore } from '@/store/userGlobal';
import { useDateTimeStore } from '@/store/dateTimeStore';

const dUrl = UrlGlobal()
const userStore = userGlobalStore()
const dateTimeStore = useDateTimeStore();

//props y emits
const props = defineProps({
    BdatosE: Boolean,
    numembarque: String
})
const emits = defineEmits(['DEpropsValue'])
const handleClick = () => {
    emits("DEpropsValue", !props.BdatosE)
}

// Referencias para el carrusel y la firma
const carouselRef = ref<HTMLElement | null>(null);
const canvasRef = ref<HTMLCanvasElement | null>(null);
const firmaPad = ref<SignaturePad | null>(null);
const firmaBase64 = ref<string | null>(null);

// Variables para la cámara de Matrícula
const video1 = ref<HTMLVideoElement | null>(null);
const canvas1 = ref<HTMLCanvasElement | null>(null);
const photo1 = ref<string | null>(null);
const isCameraActive1 = ref(false);
let stream1: MediaStream | null = null;

// Variables para la cámara de Cédula
const video2 = ref<HTMLVideoElement | null>(null);
const canvas2 = ref<HTMLCanvasElement | null>(null);
const photo2 = ref<string | null>(null);
const isCameraActive2 = ref(false);
let stream2: MediaStream | null = null;

// Variables para manejar cámaras disponibles
const cameras = ref<MediaDeviceInfo[]>([]);
const currentCameraIndex1 = ref(0); // Índice para la cámara de Matrícula
const currentCameraIndex2 = ref(0); // Índice para la cámara de Cédula

// Listar cámaras disponibles
const listCameras = async () => {
    try {
        await navigator.mediaDevices.getUserMedia({ video: true }); // Solicitar permisos
        const devices = await navigator.mediaDevices.enumerateDevices();
        cameras.value = devices.filter(device => device.kind === 'videoinput');
        if (cameras.value.length > 0) {
            currentCameraIndex1.value = 0; // Cámara por defecto para Matrícula
            currentCameraIndex2.value = 0; // Cámara por defecto para Cédula
        }
    } catch (error) {
        console.error('Error al obtener las cámaras:', error);
        alert('No se pudieron listar las cámaras. Asegúrate de conceder permisos.');
    }
};

// Iniciar cámara
const startCamera = async (camNumber: number) => {
    const video = camNumber === 1 ? video1 : video2;
    const setPhoto = camNumber === 1 ? photo1 : photo2;
    const setIsCameraActive = camNumber === 1 ? isCameraActive1 : isCameraActive2;
    let stream = camNumber === 1 ? stream1 : stream2;
    const currentCameraIndex = camNumber === 1 ? currentCameraIndex1 : currentCameraIndex2;

    try {
        setPhoto.value = null; // Limpiar foto previa
        setIsCameraActive.value = true;

        const constraints = cameras.value.length > 0 && currentCameraIndex.value < cameras.value.length
            ? { video: { deviceId: { exact: cameras.value[currentCameraIndex.value].deviceId } } }
            : { video: { facingMode: 'environment' } };

        stream = await navigator.mediaDevices.getUserMedia(constraints);
        if (video.value) {
            video.value.srcObject = stream;
        }

        if (camNumber === 1) stream1 = stream;
        else stream2 = stream;
    } catch (error) {
        console.error(`Error al iniciar cámara ${camNumber}:`, error);
        alert(`No se pudo iniciar la cámara ${camNumber}. Verifica los permisos o la disponibilidad de la cámara.`);
        setIsCameraActive.value = false;
    }
};

// Cambiar cámara
const changeCamera = async (camNumber: number) => {
    const stream = camNumber === 1 ? stream1 : stream2;
    const currentCameraIndex = camNumber === 1 ? currentCameraIndex1 : currentCameraIndex2;

    if (cameras.value.length <= 1) {
        alert('Solo hay una cámara disponible.');
        return;
    }

    if (stream) {
        stream.getTracks().forEach(track => track.stop());
    }

    currentCameraIndex.value = (currentCameraIndex.value + 1) % cameras.value.length;
    await startCamera(camNumber);
};

// Tomar foto
const takePicture = (camNumber: number) => {
    const video = camNumber === 1 ? video1.value : video2.value;
    const canvas = camNumber === 1 ? canvas1.value : canvas2.value;
    const setPhoto = camNumber === 1 ? photo1 : photo2;
    const setIsCameraActive = camNumber === 1 ? isCameraActive1 : isCameraActive2;
    let stream = camNumber === 1 ? stream1 : stream2;

    if (video && canvas && stream) {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext('2d');
        if (context) {
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            setPhoto.value = canvas.toDataURL('image/png');
        }

        stream.getTracks().forEach(track => track.stop());
        stream = null;
        setIsCameraActive.value = false;

        if (camNumber === 1) stream1 = null;
        else stream2 = null;
    }
};

// Eliminar foto
const removePhoto = (camNumber: number) => {
    const setPhoto = camNumber === 1 ? photo1 : photo2;
    const setIsCameraActive = camNumber === 1 ? isCameraActive1 : isCameraActive2;
    let stream = camNumber === 1 ? stream1 : stream2;

    setPhoto.value = null;
    setIsCameraActive.value = false;
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        stream = null;
        if (camNumber === 1) stream1 = null;
        else stream2 = null;
    }
};

// Ajustar tamaño del canvas para la firma
const resizeCanvas = () => {
    const canvas = canvasRef.value;
    if (!canvas) return;
    const ratio = window.devicePixelRatio || 1;
    canvas.width = canvas.offsetWidth * ratio;
    canvas.height = canvas.offsetHeight * ratio;
    canvas.getContext('2d')?.scale(ratio, ratio);
};

// Limpiar firma
const limpiarFirma = () => {
    firmaPad.value?.clear();
    firmaBase64.value = null;
};

async function enviarDatos() {
    const result = await question(
        'Se guardaran los datos de entrega del embarque:'+ props.numembarque,
        '¿Deseas guardar los datos?'
    )

    if (!result.isConfirmed) {
        // Usuario canceló, salimos de la función
        return
    }
    console.log(firmaPad.value)
    if (firmaPad.value && !firmaPad.value.isEmpty() && photo1.value && photo1.value.trim() !== "" && photo2.value && photo2.value.trim() !== "") {
        firmaBase64.value = firmaPad.value.toDataURL('image/png')
        const data = {
            matricula: photo1.value,
            cedula: photo2.value,
            firma: firmaBase64.value,
            no_embarque: props.numembarque,
            modificado_por: userStore.globalUser,
            fecha_status: dateTimeStore.formattedDate,
            hora_status: dateTimeStore.formattedTime
        }
        try {
            const response = await fetch(dUrl.urlGlobal + '/api2/guardar-imagenes', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            if (response.ok) {
                success('Los archivos fueron guardados correctamente.', 'Guardado exitoso')
            } else {
                error('Ocurrió un error al guardar los archivos.')
            }
        } catch (err: any) {
            error(err.response?.data?.detail || 'Ocurrió un error al guardar los datos.')
        }
        /*await fetch(dUrl.urlGlobal + "/api2/guardar-imagenes/", {
            method: "POST",
            body: formData
        });*/
    } else if (firmaPad.value) {
        warning('No ingreso la firma digital', 'Ingrese la firma')
        return
    } else if (photo1.value == null) {
        warning('Imagen de matricula no capturada', 'Capture imagen de matricula')
    } else if (photo2.value == null) {
        warning('Imagen de cedula no capturada', 'Capture imagen de cedula')
    }
}
// Montar componente
onMounted(() => {
    listCameras();

    const carouselElement = carouselRef.value;
    if (carouselElement) {
        const carousel = new Carousel(carouselElement, {
            ride: false, // Desactivar deslizamiento automático
            touch: false
        });

        carouselElement.addEventListener('slid.bs.carousel', (event: any) => {
            const activeIndex = Array.from(carouselElement.querySelectorAll('.carousel-item')).findIndex(
                (item: any) => item.classList.contains('active')
            );

            if (activeIndex === 2 && canvasRef.value) {
                resizeCanvas();
                if (!firmaPad.value) {
                    firmaPad.value = new SignaturePad(canvasRef.value);
                }
            }
        });
    }
});

// Limpiar al desmontar componente
onUnmounted(() => {
    if (stream1) stream1.getTracks().forEach(track => track.stop());
    if (stream2) stream2.getTracks().forEach(track => track.stop());
});
</script>

<style scoped>
.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    /* Fondo oscuro semitransparente */
    z-index: 1050;
    /* Coloca el fondo oscuro por encima de otros elementos */

}

.ReportPage {
    min-height: 95%;
    width: 95%;
    background: whitesmoke;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 5px;
    display: flex;
    justify-content: left;
    align-items: left;
    display: flex;
    flex-direction: column;
    gap: 15px;
    font-family: Trebuchet MS;
    color: black;
    padding: 15px;
    z-index: 1060;
    overflow: scroll;
}

.layout {
    position: absolute;
    width: 95%;
    height: 95%;

    display: grid;
    grid:
        "header" auto "container" 1fr / 1fr;
    gap: 5px;
}

.header {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    grid-area: header;
}

.header button {
    position: absolute;
    right: 0;
    padding-right: 10px;
    border: none;
    border-radius: 20px;
    background-color: transparent;
}

.container {
    grid-area: container;
}

.devices {
    justify-content: center;
    align-items: center;
    display: flex;
    overflow: hidden;
}

.devices div {
    justify-content: center;
    align-items: center;
    display: flex;
    width: 400px;
    height: 250px;
    border: 1px solid black;
    margin: 4px;
}

/* Tamaño uniforme para video, img y canvas */
.media-box {
    width: 400px;
    height: 250px;
    object-fit: cover;
    /* Hace que se recorte bien sin deformar */
}

.canvasFirm {
    touch-action: none;
    /* Evita scroll mientras se firma */
    width: 100%;
    height: 100%;
    display: block;
}

.btn-group {
    width: min-content;
    display: flex;
    justify-content: flex-end;
    gap: 20px;
    margin-top: 20px;
    padding: 5px;
    background-color: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
    border: none;
    border-radius: 10px;
    flex-direction: column;
}

.btn-group button {
    border: none;
    border-radius: 20px;
    background-color: transparent;
    transition: transform 0.2s ease;
}

.btn-group button:active {
    transform: scale(0.95);
}

.btn-group button:hover {
    border: 1px solid black;
    border-radius: 20px;
}

.custom-control {
    width: 5%;
    top: 50%;
    transform: translateY(-50%);
    z-index: 10;
}

.carousel-control-prev {
    left: 0;
    padding-left: 10px;
}

.carousel-control-next {
    right: 0;
    padding-right: 10px;
}
</style>