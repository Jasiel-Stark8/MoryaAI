<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Sidebar from './views/SideBar.vue'
</script>

<template>
  <div id="app">
    <sidebar />
    <RouterView />
  </div>
</template>

<style scoped>
#app {
  font-family: 'Roboto' sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

body {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  width: 100%;
}
</style>
