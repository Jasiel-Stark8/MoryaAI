/*import Vue from "vue";
import App from "./App.vue";
import router from "./router";

/*new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");*/

import { createApp } from "vue";
import App from "./App.vue";
//import HomePage from "./components/HomePage.vue";
//import SignUp from "./components/SignUp.vue";
import store from "./store";
createApp(App).use(store).mount("#app");
