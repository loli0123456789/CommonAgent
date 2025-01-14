<script setup lang="ts">
import { ref,onMounted,onUnmounted } from 'vue'
import { useLayoutStore } from '../stores/layout'

const isMenuOpen = ref(true) // 默认PC端展开
const isMobile = ref(false)
const layoutStore = useLayoutStore()

onMounted(() => {
  layoutStore.checkMobile()
  window.addEventListener('resize', layoutStore.checkMobile)
})

onUnmounted(() => {
  window.removeEventListener('resize', layoutStore.checkMobile)
})

const navItems = [
  { name: '首页', path: '/' },
  { 
    name: 'AI',
    children: [
      { name: 'AI Chat', path: '/chat' }
    ]
  },
  { 
    name: '系统管理',
    children: [
      { name: '用户管理', path: '/users' }
    ]
  },
  { name: '关于', path: '/about' },
  { name: '文档', path: '/docs' },
  { name: 'API', path: '/docs/api' }
]
</script>

<template>
  <div class="menu-toggle" @click="layoutStore.toggleMenu">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M3 18H21V16H3V18ZM3 13H21V11H3V13ZM3 6V8H21V6H3Z" fill="currentColor"/>
    </svg>
  </div>
  <nav class="navbar" :class="{ 'active': layoutStore.isMenuOpen }">
    <div class="container">
      <router-link to="/" class="logo">CommonAgent</router-link>
      <ul class="nav-list">
        <li v-for="item in navItems" :key="item.path || item.name" class="nav-item">
          <template v-if="item.children">
            <div class="nav-group">
              <span class="nav-group-title">{{ item.name }}</span>
              <ul class="nav-sub-list">
                <li v-for="child in item.children" :key="child.path" class="nav-sub-item">
                  <router-link :to="child.path" class="nav-link">
                    {{ child.name }}
                  </router-link>
                </li>
              </ul>
            </div>
          </template>
          <template v-else>
            <router-link :to="item.path" class="nav-link">
              {{ item.name }}
            </router-link>
          </template>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.menu-toggle {
  position: fixed;
  top: 1rem;
  left: 0rem;
  z-index: 1001;
  cursor: pointer;
  padding: 0.5rem;
  background: var(--color-background);
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  display: block; /* 始终显示 */
}

.navbar {
  width: 250px;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  background: var(--color-background-soft);
  border-right: 1px solid var(--color-border);
  transition: transform 0.3s ease;
  z-index: 1000;
  transform: translateX(-100%); /* 默认隐藏 */
}

.navbar.active {
  transform: translateX(0);
}

@media (max-width: 768px) {
  .navbar {
    transform: translateX(-100%);
    width: 50%; /* 移动端下设置为全屏宽度 */
  }

  .menu-toggle {
    /* 移动端时调整位置，避免被header遮挡 */
    top: 70px; /* 根据你的header高度调整 */
  }
}

.container {
  padding: 2rem 1rem;
}

.logo {
  display: block;
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 2rem;
  text-align: center;
  color: var(--color-heading);
  text-decoration: none;
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  margin: 0.5rem 0;
}

.nav-group-title {
  display: block;
  padding: 0.75rem 1rem;
  color: var(--color-text);
  font-weight: 500;
}

.nav-sub-list {
  list-style: none;
  padding: 0;
  margin: 0.5rem 0 0 1rem;
}

.nav-sub-item {
  margin: 0.25rem 0;
}

.nav-link {
  display: block;
  padding: 0.75rem 1rem;
  border-radius: 4px;
  color: var(--color-text);
  text-decoration: none;
  transition: background 0.2s;
}

.nav-link:hover {
  background: var(--color-background-mute);
}

.router-link-active {
  background: var(--color-background-mute);
  font-weight: bold;
}
</style>