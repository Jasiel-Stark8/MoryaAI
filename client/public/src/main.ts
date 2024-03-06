/* eslint-disable vue/multi-word-component-names */
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'

import PrimeVue from 'primevue/config'
import 'primevue/resources/themes/saga-blue/theme.css' //theme
import 'primevue/resources/primevue.min.css' //core CSS
import 'primeicons/primeicons.css' //icons
import '/node_modules/primeflex/primeflex.css'
import Calendar from 'primevue/calendar'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import Sidebar from 'primevue/sidebar'
import RadioButton from 'primevue/radiobutton';
import MultiSelect from 'primevue/multiselect';


import router from './router'
import './index.css'
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(PrimeVue)
app.component('Calendar', Calendar)
app.component('InputText', InputText)
app.component('Sidebar', Sidebar)
app.component ('RadioButton', RadioButton)
app.component('MultiSelect', MultiSelect)
app.mount('#app')
