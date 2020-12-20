import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSlideoutPanel from 'vue2-slideout-panel';
import vueMoment from 'vue-moment'
Vue.use(vueMoment)
Vue.use(VueSlideoutPanel);
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
