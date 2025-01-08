<script setup lang="ts">
</script>

<template>
  <header class="header">
    <div class="container">
      <div class="logo">CommonAgent</div>
      <div class="auth-links">
        <router-link to="/login" class="auth-link">登录</router-link>
        <span class="divider">|</span>
        <router-link to="/register" class="auth-link">注册</router-link>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header {
  background: #1e3c72;
  color: white;
  padding: 1rem;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.2rem;
  font-weight: bold;
}

.auth-links {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.auth-link {
  color: white;
  text-decoration: none;
  font-weight: 500;
  transition: opacity 0.2s;
}

.auth-link:hover {
  opacity: 0.8;
}

.divider {
  color: rgba(255, 255, 255, 0.5);
}
</style>