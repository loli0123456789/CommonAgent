<script setup lang="ts">
import Header from './components/Header.vue'
import NavBar from './components/NavBar.vue'
</script>

<template>
  <div class="app">
    <Header />
    <div class="main-layout">
      <NavBar />
      <main class="main-content">
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

html, body {
  /* height: 100%; */
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
  padding-left: 250px;
  width: 100%; /* 确保父容器宽度为100% */
}

.main-content {
  flex: 1;
  padding: 1rem;
  width: calc(100% - 250px);
  overflow: auto;
}
</style>
