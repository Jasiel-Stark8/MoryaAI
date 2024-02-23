//comment to be added
import Vue from "vue";
import Router from "vue-router";

// Import your Vue components here
import HomePage from "./components/HomePage.vue";
import SignUp from "./components/SignUp.vue";


// Import other components as needed

Vue.use(Router);

export default new Router({
routes: [
    { 
        path: "/HomePage",
        name: "HomePage",
        component: Homepage
    },
    {
        path: "/SignUp",
        name: "SignUp",
        component: SignUp
    },
    {
        path: "/LogIn",
        name: "LogIn",
        component: LogIn
    },
]
});
