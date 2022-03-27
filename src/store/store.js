import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex)

import test from './test'

const store = new Vuex.Store[{
    module: {
        test
    }
}]

export default store;

// import { createStore } from 'vuex';

// const store = createStore({
//     state(){
//         return{
            
//         }
//     }
// })

// export default store;