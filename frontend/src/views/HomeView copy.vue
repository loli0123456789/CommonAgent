<script setup lang="ts">
import { ref } from 'vue'
import PlatformIntro from '../components/PlatformIntro.vue'
import CoreFeatures from '../components/CoreFeatures.vue'
import QuickStart from '../components/QuickStart.vue'

const features = ref([
  {
    title: '多模型API集成',
    description: '支持OpenAI、Anthropic等主流模型API的统一接入',
    icon: 'model'
  },
  {
    title: '智能工具管理', 
    description: '可视化配置工具，支持自动选择和手动选择',
    icon: 'tool'
  },
  {
    title: '场景化应用支持',
    description: '提供标准API接口，支持与业务系统深度集成',
    icon: 'integration'
  }
])
</script>

<template>
  <div class="home-view">
    <PlatformIntro />
    
    <section class="features-section">
      <h2 class="section-title">核心功能</h2>
      <CoreFeatures :features="features" />
    </section>

    <section class="quickstart-section">
      <h2 class="section-title">快速开始</h2>
      <QuickStart />
    </section>

    

    <footer class="footer">
      <router-link to="/docs/api">API文档</router-link>
    </footer>
  </div>
</template>

<style scoped>
.home-view {
  width: 100%;
  height: 100%;
  padding: 4rem 2rem 2rem;
  display: flex;
  flex-direction: column;
  overflow: auto;
}

.section-title {
  margin: 2rem 0 1rem;
  font-size: 1.5rem;
  color: var(--color-heading);
}

.features-section {
  margin: 3rem 0;
}

.quickstart-section {
  margin: 3rem 0;
}

.footer {
  margin-top: 4rem;
  padding: 1rem 0;
  border-top: 1px solid var(--color-border);
  text-align: center;
}
</style>
