<!-- Signin.vue -->

<template>
  <!-- Form Image-->
  <a
    href="#"
    class="a flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700"
  >
    <img
      class="object-cover w-full rounded-t-lg h-96 md:h-auto md:w-48 md:rounded-none md:rounded-s-lg"
      src="https://i.pinimg.com/736x/7f/00/16/7f00163c114a7b3bfe3a3a65e5d5ea94.jpg"
      alt="login"
    />
    <div class="login-page flex-col justify-between p-8 leading-normal border-gray-200 shadow">
      <h2 class="text-5xl font-bold dark:text-white">Welcome back!</h2>

      <!-- Login form -->
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="username">Username or Email:</label>
          <input
            type="text"
            id="username"
            v-model.trim="username"
            placeholder="Username"
            required
          />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model.trim="password"
            placeholder="Password"
            required
          />
        </div>

        <!-- Submit -->
        <button type="submit">Login</button>
        <p>
          Don't have an account<br />
          <span>
            <router-link to="/signup"> Sign up </router-link>
          </span>
        </p>
      </form>
    </div>
  </a>
</template>

<script lang="ts">
export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async handleLogin() {
      try {
        // Make an API call to authenticate the user
        const response = await fetch('/api/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          })
        })

        if (response.ok) {
          // Login successful
          // Redirect to the dashboard page
          const router = useRouter()
          router.push('/') // Change the route path as needed
        } else {
          // Handle login error (e.g., display an error message)
          console.error('Login failed')
        }
      } catch (error) {
        console.error('An error occurred during login:', error)
      }
    }
  }
}
</script>

<style scoped>
.a {
  margin-left: 5em;
  align-items: center;
}

.login-page {
  align-items: center;
  width: 700px;
  height: 600px;
  background-color: #220135ca;
}

.form-group {
  padding-bottom: 1px;
}

h2 {
  margin-bottom: 1em;
  padding-top: 1em;
  color: #fbfaff;
}

p {
  color: #fbfaff;
  padding: 1em;
}

div {
  padding-left: 1em;
}

p span {
  color: #4094ed;
  margin: 0 auto;
}

label {
  display: block;
  margin-top: 0.5em;
  padding-bottom: 6px;
  font-size: 1.2em;
  color: #fbfaff;
}

input[type='text'],
input[type='password'] {
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ccccccfb;
  width: 300px;
  color: grey;
}

button {
  background-color: #007bff;
  color: #fff;
  margin: 1.5em;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0057b35f;
}
</style>
