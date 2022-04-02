import { createApp } from 'vue'
import App from './App.vue'
import routers from './routers/router.js'
import WebCam from 'vue-web-cam';
// import store from './store/store'

createApp(App).use(routers).use(WebCam).mount('#app')
