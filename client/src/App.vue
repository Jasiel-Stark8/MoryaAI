<template>
  <HomePage />
  <SignUp />
  <LogIn />
</template>

<script>
import HomePage from "./components/HomePage.vue";
import SignUp from "./components/SignUp.vue";
import LogIn from "./components/LogIn.vue";

export default {
  name: "App",
  components: {
    HomePage,
    SignUp,
    LogIn,
  },
};
</script>

<style>
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
