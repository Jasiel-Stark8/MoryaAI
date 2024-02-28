<!-- Login.vue -->

<template>
  
<a href="#" class=" a flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700">
    <img class="object-cover w-full rounded-t-lg h-96 md:h-auto md:w-48 md:rounded-none md:rounded-s-lg" src="https://i.pinimg.com/736x/7f/00/16/7f00163c114a7b3bfe3a3a65e5d5ea94.jpg" alt="login">
      <div class="login-page flex-col justify-between p-8 leading-normal border-gray-200 shadow ">
        <h2 class=" text-5xl font-bold   dark:text-white">Log In</h2>
          <form @submit.prevent="login">
        <div class="form-group">
          <label for="username">Username or Email:</label>
          <input type="text" id="username" v-model.trim="username" required>
        </div>
        <div class="form-group">
          <label for="password" class="text-1xl">Password:</label>
          <input type="password" id="password" v-model.trim="password" required>
        </div>
        <button type="submit">Login</button>
        <p>Don't have an account<br> 
          <span>
            <router-link to="/signup">
            Sign up
            </router-link>
          </span>
        </p>
      </form>
    </div>
</a>
</template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      login() {
        // Implement login logic here
        console.log('Welcome Back!');
      }
    }
  };
  </script>
  
  <style scoped>

  .a{
    margin-left: 5em;
    align-items: center;
  }

  .login-page {
    align-items: center;
    width: 700px;
    height: 600px;
    background-color: #f7ede29a;
    
  }
  
  .form-group {
    padding-bottom: 1px;
    margin-top: 1.5em;
  }

h2 {
    margin-bottom: 0;
    padding-top: 1em;
    color: #1b263be4;
  }

  p {
    color: #2b2d42;
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
    margin-bottom: 5px;
    color: #2b2d42;
  }
  
  input[type="text"],
  input[type="password"] {
    padding: 8px;
    border-radius: 4px;
    border: 1px solid #ccccccfb;
    width: 300px;
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
  