import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

router.beforeEach((to, from, next) => {
    // 设置页面标题
    document.title = to.meta.title as string || 'Common Agent';
    next();
  });

app.use(createPinia())
app.use(router)

app.mount('#app')
