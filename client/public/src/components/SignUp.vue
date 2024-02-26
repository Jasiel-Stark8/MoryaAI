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
    }
  },
  methods: {
    submitForm() {
      // Implement form submission logic here
      console.log('Form submitted with data:', this.formData)
    }
  },
}
</script>

<template>
  <div class="signup-form">
    <h2>Sign Up</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <FloatLabel>
          <label for="username">Username</label>
          <InputText type="text" id="username" v-model.trim="formData.username" required />
        </FloatLabel>
      </div>

      <div class="form-group">
        <FloatLabel>
          <label for="firstName">First Name</label>
          <InputText type="text" id="firstName" v-model.trim="formData.firstName" required />
        </FloatLabel>
      </div>

      <div class="form-group">
        <FloatLabel>
          <label for="middleName">Middle Name</label>
          <InputText type="text" id="middleName" v-model.trim="formData.middleName" />
        </FloatLabel>
      </div>

      <div class="form-group">
        <FloatLabel>
          <label for="lastName">Last Name</label>
          <InputText type="text" id="lastName" v-model.trim="formData.lastName" required />
        </FloatLabel>
      </div>

      <div class="form-group">
        <FloatLabel>
          <label for="birth_date">Birth Date</label>
          <Calendar v-model="date" inputId="birth_date" />
        </FloatLabel>
      </div>

      <div class="form-group">
        <label for="gender">Gender</label>
        <select id="gender" v-model="formData.gender" required>
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </div>

      <div class="form-group">
        <FloatLabel>
          <label for="email">Email</label>
          <InputText type="email" id="email" v-model.trim="formData.email" required />
        </FloatLabel>
      </div>

      <div class="form-group">
        <FloatLabel>
          <label for="password">Password</label>
          <InputText type="password" id="password" v-model.trim="formData.password" required />
        </FloatLabel>
      </div>
      <div class="card flex justify-content-center">
        <Button label="Submit" />
    </div>
    </form>
  </div>
</template>

<style scoped>
.signup-form {
  max-width: 400px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 20px;
  display: flex;
  flex-wrap: wrap;
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
