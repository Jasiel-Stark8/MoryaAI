<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div id="app">
    <RouterView />
  </div>
</template>

<style scoped>
#app {
  font-family: 'Roboto' sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-OSX-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>