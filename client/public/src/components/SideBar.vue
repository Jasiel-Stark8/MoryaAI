<script setup lang="ts">
</script>


<template>
    <div class="sidebar">xp
        <div class="title">
            Side Bar
        </div>
        <div class="menu-items">
            <RouterLink to="/" active-class="active">
                <div class="link-container">
                    Dashboard
                </div>
            </RouterLink>
            <RouterLink to="/GenerationPage" active-class="active">
                <div class="link-container">
                    Sign In
                </div>
            </RouterLink>
            <RouterLink to="/signup" active-class="active">
                <div class="link-container">
                    Sign Up
                </div>
            </RouterLink>
            <RouterLink to="/SignIn" active-class="active">
                <div class="link-container">
                    Sign In
                </div>
            </RouterLink>
        </div>
        <RouterLink to="/ProfilePage" active-class="active">
            <div class="link-container">
                Profile
            </div>
        </RouterLink>
    </div>
</template>
