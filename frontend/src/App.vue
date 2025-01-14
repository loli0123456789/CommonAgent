<script setup lang="ts">
import Header from './components/Header.vue'
import NavBar from './components/NavBar.vue'
import { useLayoutStore } from './stores/layout'

const layoutStore = useLayoutStore()
</script>

<template>
  <div class="app">
    <Header />
    <div class="main-layout">
      <NavBar />
      <main class="main-content" :class="{ 'nav-hidden': !layoutStore.isMenuOpen }">
        <router-view />
      </main>
    </div>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%; /* 确保.app容器宽度为100% */
}

.main-layout {
  display: flex;
  flex: 1;
  margin-top: 60px;
  /* 删除这行，因为已经在 main-content 中设置了 padding */
  /* padding-left: 250px; */
  width: 100%;
}

.main-content {
  position: relative;
  min-height: 100vh;
  width: 100%;
  padding-left: 250px;
  box-sizing: border-box;
  transition: padding-left 0.3s ease;
}

/* 添加导航隐藏时的样式 */
.main-content.nav-hidden {
  padding-left: 0;
}

@media (max-width: 768px) {
  .main-layout {
    /* 确保移动端时布局正确 */
    padding-left: 0;
  }
  
  .main-content {
    padding-left: 0;
  }
}

</style>
