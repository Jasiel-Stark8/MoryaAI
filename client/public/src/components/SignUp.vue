<!-- Signup.vue -->

<script lang='ts'>
import { useRouter } from 'vue-router';
import { ref, watch } from 'vue';
import { today } from 'date-fns';

export default {
  data() {
    return {
      formData: {
        Username: '',
        Name: '',
        age: '',
        gender: '',
        email: '',
        password: '',
      },
      isLoading: false, // Flag to indicate loading state
      errorMessage: '', // Store error message if registration fails
      validationErrors: {},
    };
  },
  methods: {
    async handleSignUp() {
      this.validationErrors = {}; // Clear previous validation errors
      const isValid = this.validateForm();

      if (isValid) {
        this.isLoading = true;
        this.errorMessage = '';

        try {
          const response = await fetch('/api/signup', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.formData),
          });

          if (response.ok) {  // Redirect to dashboar
            this.router.push('/');
} else {
const errorData = await response.json(); // Parse error message
this.errorMessage = errorData.message || 'Registration failed'; // error message
}
} catch (error) {
console.error('An error occurred during registration:', error);
this.errorMessage = 'An unexpected error occurred. Please try again later.'; // error message for user
} finally {
this.isLoading = false; // Reset loading state regardless of success or failure
}
}
},
validateForm() {
const hasRequiredFields = Object.values(this.formData).every(
(value) => value.trim() !== ''
);
const isValidName = this.validateName(this.formData.Name);                // For client-side name validation
const isValidPassword = this.validatePassword(this.formData.password);    // For client-side password validation
const isValidAge = this.validateAge(this.formData.age);                   // For client-side age validation  
const isValidEmail = this.validateEmail(this.formData.email);             // For client-side email validation  
return (
hasRequiredFields &&
isValidName &&
isValidPassword &&
isValidAge &&
isValidEmail
); // All validations must pass
},
// Validate name
validateName(name) {
      const nameParts = name.trim().split(/\s+/); // Split on whitespace
      const isValidLength = nameParts.length >= 1 && nameParts.length <= 3;
      const isValidCharacters = nameParts.every((part) => /^[a-zA-Z]+$/.test(part)); // Only letters allowed
      const errorMessage = 'Name must contain only letters (1-3 names)';
      if (!isValidLength || !isValidCharacters) {
        this.validationErrors.name = errorMessage;
        return false;
      }
      return true;
    },
    // Validate age
    validateAge(age) {
      const minAge = 15;
      const todayDate = new Date();

      try {
        const birthYear = todayDate.getFullYear() - parseInt(age);
        const birthDate = new Date(birthYear, todayDate.getMonth(), todayDate.getDate());
        return birthDate <= todayDate;
      } catch (error) {
        console.error('Error during age validation:', error);
        // Handle potential parsing errors gracefully (e.g., invalid age input)
        this.validationErrors.age = 'Invalid age entered. Please try again.';
        return false;
      }
    },
    // Validate email
    validateEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email format validation
      const advancedEmailRegex = /^(([^<>()[\\]\\\\.,;:\s@"]+(\.[^<>()[\\]\\\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return emailRegex.test(email);
      return advancedEmailRegex.test(email);
    },
    // Validate Password
    validatePassword(password) {
      const minLength = 10;
      const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!])(?=.*\S)[^ ]{10,}$/; // Consider adjusting requirements
      return password.length >= minLength && passwordRegex.test(password);
    },
  },
};

</script>
<template>
  <div class="ml-7">
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
            <label for="username">Username</label>
            <InputText
              type="text"
              id="username"
              v-model.trim="formData.username"
              required='red'
              placeholder="Username"
            />
          </FloatLabel>
        </div>
        <div class="form-group 1-2">
          <FloatLabel>
            <label for="Name">Name</label>
            <InputText
              type="text"
              id="Name"
              v-model.trim="formData.Name"
              required
              placeholder="Enter your Name"
            />
          </FloatLabel>
        </div>
        <div class="form-group l-1">
          <FloatLabel>
            <label for="age">Age</label>
            <Calendar v-model="age" inputId="age" placeholder="Enter birth date" required/>
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
</div>
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
