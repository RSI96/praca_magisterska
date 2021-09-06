import Vue from 'vue'
import App from './App.vue'
import router from './router'
//import HighchartsVue from 'highcharts-vue'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'

Vue.config.productionTip = false
//Vue.use(HighchartsVue)

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
