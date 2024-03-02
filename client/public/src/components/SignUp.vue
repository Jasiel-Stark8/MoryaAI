<!-- Signup.vue -->
<script lang="ts">
import { useRouter } from 'vue-router'
export default {
  data() {
    return {
      formData: {
        firstName: '',
        middleName: '',
        lastName: '',
        age: null,
        gender: '',
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async handleSignUp() {
      try {
        // Make an API call to register the user
        const response = await fetch('/api/signup', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.formData)
        })

        if (response.ok) {
          // Registration successful
          // Redirect to the dashboard page
          const router = useRouter()
          router.push('/') // route path
        } else {
          // Handle registration error (e.g., display an error message)
          console.error('Registration failed')
        }
      } catch (error) {
        console.error('An error occurred during registration:', error)
      }
    }
  }
}
</script>

<template>
  <!-- Form images -->
  <a
    href="#"
    class="flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700"
  >
    <img
      class="object-cover w-full rounded-t-lg h-96 md:h-auto md:w-48 md:rounded-none md:rounded-s-lg"
      src="https://i.pinimg.com/736x/0e/30/15/0e301569d3dbf7290b718317ed97fe80.jpg"
      alt="login"
    />
    <div class="signup-form p-8 leading-normal border-gray-200 shadow">
      <h2 class="text-5xl font-bold dark:text-white">Sign Up</h2>

      <!-- Signup form -->
      <form @submit.prevent="submitForm">
        <div class="form-group l-1">
          <FloatLabel>
            <label for="username">Username </label>
            <InputText
              type="text"
              id="username"
              v-model.trim="formData.username"
              required
              placeholder="Username"
            />
          </FloatLabel>
        </div>
        <div class="form-group 1-2">
          <FloatLabel>
            <label for="firstName">Full Name </label>
            <InputText
              type="text"
              id="firstName"
              v-model.trim="formData.firstName"
              required
              placeholder="Full Name"
            />
          </FloatLabel>
        </div>
        <div class="form-group l-1">
          <FloatLabel>
            <label for="birth_date">Birth Date</label>
            <Calendar v-model="date" inputId="birth_date" placeholder="Enter birth date" />
          </FloatLabel>
        </div>
        <div class="form-group l-2">
          <label for="gender">Gender</label>
          <select id="gender" v-model="formData.gender" required>
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div class="form-group l-1">
          <FloatLabel>
            <label for="email">Email</label>
            <InputText
              type="email"
              id="email"
              v-model.trim="formData.email"
              placeholder="Enter your email"
              required
            />
          </FloatLabel>
        </div>
        <div class="form-group l-2">
          <FloatLabel>
            <label for="password"> Password </label>
            <InputText
              type="password"
              id="password"
              v-model.trim="formData.password"
              placeholder="Enter password"
              required
            />
          </FloatLabel>
        </div>
        <div class="card flex justify-content-center">
          <Button @click="handleSignUp" label="Submit">Submit </Button>
        </div>
        <p class="mb-3 font-normal text-gray-100 dark:text-gray-100">
          Have an account?<br />Log In
          <router-link to="/signin" class="mb-3 font-normal text-blue-900 dark:text-blue-900"
            ><span>here</span></router-link
          >
        </p>
      </form>
    </div>
  </a>
</template>

<style scoped>
a {
  margin-left: 5em;
  margin: 0 auto;
}
.signup-form {
  background-color: #2a0447bf;
}

form {
  margin-top: 1.5em;
  width: 450px;
  height: 350px;
  align-items: center;
}

h2 {
  color: #f6f2d6eb;
}

p {
  padding: 1em;
}

p span {
  color: #419dff;
}

.form-group {
  margin-bottom: 20px;
}

.l-1 {
  position: relative;
  float: left;
  padding-left: 1.5em;
}

label {
  display: block;
  margin-bottom: 5px;
  font-size: 1.2em;
  color: #efe5b8e5;
  align-items: flex-start;
  padding-right: 1em;
}

input,
select {
  width: 200px;
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ccc;
  color: #0000009c;
}

button {
  background-color: #4094ed;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
