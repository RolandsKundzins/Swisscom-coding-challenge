import { createApp } from 'vue'
import App from './App.vue'
import '@swisscom/sdx/dist/css/sdx.css';
import { defineCustomElements } from '@swisscom/sdx/dist/js/webcomponents/loader';

defineCustomElements(window);

createApp(App).mount('#app')
