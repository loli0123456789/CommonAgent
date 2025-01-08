<script setup lang="ts">
const title = '通用智能体平台'
const description = 'CommonAgent 是一个通用智能体平台，为开发者提供构建AI应用的统一框架和工具集'
</script>

<template>
  <section class="intro-section">
    <div class="intro-content">
      <h1 class="title">{{ title }}</h1>
      <p class="description">{{ description }}</p>
      <div class="cta-buttons">
        <router-link to="/docs" class="cta-button primary">开始使用</router-link>
        <router-link to="/docs/api" class="cta-button secondary">查看API</router-link>
      </div>
    </div>
  </section>
</template>

<style scoped>
.intro-section {
  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
  color: white;
  width: 100%;
  padding: 2rem 2rem;
  margin: 0;
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.intro-content {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}

.title {
  font-size: 3rem;
  margin-bottom: 1.5rem;
  font-weight: bold;
}

.description {
  font-size: 1.25rem;
  max-width: 800px;
  margin: 0 auto 2rem;
  line-height: 1.6;
}

.cta-buttons {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 2rem;
}

.cta-button {
  padding: 0.75rem 2rem;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.2s;
}

.cta-button.primary {
  background: white;
  color: #1e3c72;
}

.cta-button.primary:hover {
  background: #f0f0f0;
}

.cta-button.secondary {
  border: 2px solid white;
  color: white;
}

.cta-button.secondary:hover {
  background: rgba(255, 255, 255, 0.1);
}
</style>