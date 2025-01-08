<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Username</label>
        <input
          v-model="form.username"
          type="text"
          id="username"
          required
        />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input
          v-model="form.password"
          type="password"
          id="password"
          required
        />
      </div>
      <button type="submit">Login</button>
    </form>
    <p>
      Don't have an account? 
      <router-link to="/register">Register here</router-link>
    </p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authService } from '@/services/api'

const router = useRouter()

const form = ref({
  username: '',
  password: ''
})

const handleLogin = async () => {
  try {
    await authService.login(form.value.username, form.value.password)
    router.push('/')
  } catch (error) {
    console.error('Login failed:', error)
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 2rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 0.5rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #3aa876;
}

p {
  margin-top: 1rem;
  text-align: center;
}
</style>
