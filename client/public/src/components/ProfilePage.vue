<script lang="ts">
export default {
  data() {
    return {
      profile: {
        username: 'User Jane',
        name: 'Jane Doe',
        profession: 'Writer',
        avatar: 'https://via.placeholder.com/150', // Default avatar
      },
    };
  },
  methods: {
    handleAvatarChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = (e) => {
          this.profile.avatar = e.target.result;
        };
      }
    },
  },
  directives: {
    vCenter: {
      inserted(el) {
        const parent = el.parentElement;
        const styles = {
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100%',
        };
        Object.assign(parent.style, styles);
      },
    },
  },
};
</script>

<template>
  <div class="profile-page">
  <div class="profile-card absolute center-3 top-3" v-center >
    <div class="avatar-container flex flex-col text-gray-600 items-center">
      <img :src="profile.avatar" alt="profile picture" class="rounded-full w-24 h-24" />
      <input
        type="file"
        class="pt-1"
        accept="image/*"
        @change="handleAvatarChange"
      />
      <label for="avatar-upload" class="text-indigo-700 hover:underline cursor-pointer">
        Upload image
      </label>
    </div>
    <div class="user-info">
      <h2 class="text-2xl font-semibold text-gray-500 pt-3">{{ profile.username }}</h2>
      <h2 class="text-2xl font-semibold text-gray-700 pt-3">{{ profile.name }}</h2>
      <p class="text-gray-900 p-1">{{ profile.profession }}</p>
      </div>
  </div>
</div>
  <!-- Profile Form -->
   
</template>

<style scoped>
.profile-card {
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(50, 255, 250, 0.3);
  padding: 20px;
  margin-top: 13em;
  margin-left: -16em;
  margin-right: 2em;
  margin-bottom: 2em;
  min-width: 800px; /* min-width for responsiveness */
  max-width: 700px; /* max-width for responsiveness */
  display: flex;
  flex-direction: column;
  align-items: center;
}

.avatar-container {
  margin-bottom: 15px;
}
</style>