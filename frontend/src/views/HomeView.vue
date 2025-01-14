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

<style>
.home-view {
  width: 100%;
  margin-top: 2rem;
  padding: 0 1rem;
}

@media (max-width: 768px) {
  .home-view {
    padding: 0 1rem;
    margin-top: 4rem;
    margin-left: 0;
    width: 100%;
    position: relative;
    left: 0;
  }
}

.section-title {
  margin: 2rem 0 1rem;
  font-size: 1.5rem;
  color: var(--color-heading);
}

.features-section {
  width: 100%;
  max-width: 100%;
  overflow-x: hidden;
}

.platform-intro {
  padding: 20px;
  flex: 1;
  width: 100%;
}

.quickstart-section {
  margin: 2rem 0;
  width: 100%;
}

.footer {
  margin-top: 4rem;
  padding: 1rem 0;
  border-top: 1px solid var(--color-border);
  text-align: center;
  width: 100%;
}

</style>
