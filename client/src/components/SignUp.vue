<template>
  <div class="signup-form">
    <h2>Sign Up</h2>
    <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="firstName">First Name</label>
          <input type="text" id="firstName" v-model.trim="formData.firstName" required>
        </div>
        <div class="form-group">
          <label for="middleName">Middle Name</label>
          <input type="text" id="middleName" v-model.trim="formData.middleName">
        </div>
        <div class="form-group">
          <label for="lastName">Last Name</label>
          <input type="text" id="lastName" v-model.trim="formData.lastName" required>
        </div>
        <div class="form-group">
          <label for="age">Age</label>
          <input type="number" id="age" v-model.number="formData.age" required>
        </div>
        <div class="form-group">
          <label for="gender">Gender</label>
          <select id="gender" v-model="formData.gender" required>
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="binary">Binary</option>
            <option value="Prefer not to say">Prefer not to say</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model.trim="formData.email" required>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model.trim="formData.password" required>
        </div>
        <button type="submit">Sign Up</button>
      </form>
    </div>
</template>

<script>
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
    };
    },
    methods: {
    submitForm() {
        console.log('Form submitted with data:', this.formData);
    }
    }
};
</script>

<style scoped>
.signup-form {
    max-width: 400px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input,
select {
    width: 100%;
    padding: 8px;
    border-radius: 4px;
    border: 1px solid #ccc;
}

button {
    background-color: #007bff;
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
