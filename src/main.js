import { createApp } from 'vue'
import App from './App.vue'
import routers from './routers/router.js'
// import store from './store/store'

createApp(App).use(routers).mount('#app')
