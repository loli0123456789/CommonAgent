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
  height: 100%;
}

.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-layout {
  display: flex;
  flex: 1;
  margin-top: 100px;
  padding-left: 250px;
}

.main-content {
  flex: 1;
  padding: 2rem;
  width: calc(100% - 250px);
}
</style>
