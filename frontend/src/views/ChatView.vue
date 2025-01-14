<script setup lang="ts">
import ChatWindow from '@/components/ChatWindow.vue'
</script>

<template>
  <div class="chat-view">
    <h1>AI 对话</h1>
    <ChatWindow />
  </div>
</template>

<style scoped>
.chat-view {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}
</style>