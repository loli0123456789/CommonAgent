<script setup lang="ts">
const steps = [
  {
    title: '安装依赖',
    command: 'npm install',
    description: '安装项目所需依赖'
  },
  {
    title: '配置环境',
    command: 'cp .env.example .env',
    description: '复制环境变量配置文件并修改'
  },
  {
    title: '启动开发服务器',
    command: 'npm run dev',
    description: '启动本地开发服务器'
  },
  {
    title: '构建生产版本', 
    command: 'npm run build',
    description: '构建生产环境代码'
  }
]
</script>

<template>
  <div class="steps-container">
    <div v-for="(step, index) in steps" :key="step.title" class="step-card">
      <div class="step-header">
        <span class="step-number">Step {{ index + 1 }}</span>
        <h3 class="step-title">{{ step.title }}</h3>
      </div>
      <div class="step-content">
        <code class="step-command">{{ step.command }}</code>
        <p class="step-description">{{ step.description }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.steps-container {
  display: grid;
  gap: 1.5rem;
  max-width: 800px;
  margin: 0 auto;
}

.step-card {
  padding: 1.5rem;
  border-radius: 8px;
  background: var(--color-background-soft);
}

.step-header {
  margin-bottom: 1rem;
}

.step-number {
  display: block;
  font-size: 0.9rem;
  color: var(--color-text-soft);
}

.step-title {
  font-size: 1.1rem;
  margin: 0.25rem 0;
}

.step-command {
  display: block;
  padding: 0.5rem 1rem;
  margin: 0.5rem 0;
  background: var(--color-background-mute);
  border-radius: 4px;
  font-family: monospace;
}

.step-description {
  color: var(--color-text);
  margin: 0.5rem 0 0;
}
</style>