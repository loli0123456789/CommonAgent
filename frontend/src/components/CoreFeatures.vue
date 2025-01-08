<script setup lang="ts">
import { FeatureItem } from '../types'

defineProps<{
  features: FeatureItem[]
}>()
</script>

<template>
  <div class="features-grid">
    <div v-for="feature in features" :key="feature.title" class="feature-card">
      <div class="icon-wrapper">
        <img :src="`/icons/${feature.icon}.svg`" :alt="feature.title" />
      </div>
      <h3 class="feature-title">{{ feature.title }}</h3>
      <p class="feature-description">{{ feature.description }}</p>
    </div>
  </div>
</template>

<style scoped>
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.feature-card {
  padding: 1.5rem;
  border-radius: 8px;
  background: var(--color-background-soft);
  transition: transform 0.2s;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.icon-wrapper {
  width: 64px;
  height: 64px;
  margin: 0 auto 1rem;
}

.feature-title {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  text-align: center;
}

.feature-description {
  color: var(--color-text);
  line-height: 1.6;
}
</style>