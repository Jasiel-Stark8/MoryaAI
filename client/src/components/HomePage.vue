<template>
  <div class="navbar">
    <div class="nav-brand">
      <router-link to="/">MoryaAI</router-link>
    </div>
    <router-link to="/login" class="nav-item">Log In</router-link>
    <router-link to="/signup" class="nav-item">Sign Up</router-link>
    <router-link to="/generationPage" class="nav-item">Generate</router-link>
    <router-link to="/dashboard" class="nav-item">Dashboard</router-link>
    <router-link to="/ProfilePage" class="nav-item">Profile</router-link>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  props: {
    msg: String,
  },
};
</script>

<style scoped>
.navbar {
  background-color: #333;
  color: #fff;
  padding: 10px 20px; /* Add padding to create space around the links */
}

.nav-item {
  margin-right: 20px; /* Add margin between each navigation item */
  color: #fff;
  text-decoration: none;
}

.nav-item:hover {
  color: #fff;
  text-decoration: underline;
}
</style>
