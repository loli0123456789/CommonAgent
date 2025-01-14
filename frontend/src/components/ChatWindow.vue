<template>
  <div class="chat-window">
    <div class="messages">
      <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.role]">
        {{ msg.content }}
      </div>
    </div>
    <div class="input-area">
      <input v-model="inputText" @keyup.enter="sendMessage" placeholder="输入消息..." />
      <button @click="sendMessage">发送</button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue"
import { useChatStore } from "@/stores/chat"

interface Message {
  role: string
  content: string
}

const chatStore = useChatStore()
const inputText = ref("")
const messages = ref<Message[]>([])

const sendMessage = async () => {
  if (!inputText.value.trim()) return
  
  const userMessage: Message = { 
    role: "user", 
    content: inputText.value 
  }
  messages.value.push(userMessage)
  
  try {
    const response = await chatStore.sendMessage(inputText.value)
    const aiMessage: Message = { 
      role: "assistant", 
      content: response.response 
    }
    messages.value.push(aiMessage)
  } catch (error) {
    console.error("发送消息失败：", error)
  }
  
  inputText.value = ""
}
</script>

<style scoped>
.chat-window {
  width: 100%;
  height: 70vh;
  border: 1px solid #ccc;
  display: flex;
  flex-direction: column;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 8px;
}

.message {
  margin: 4px 0;
  padding: 6px 10px;
  border-radius: 8px;
  max-width: 80%;
}

.message.user {
  background: #e3f2fd;
  margin-left: auto;
}

.message.assistant {
  background: #f5f5f5;
  margin-right: auto;
}

.input-area {
  display: flex;
  padding: 10px;
  border-top: 1px solid #eee;
}

.input-area input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 8px;
}

.input-area button {
  padding: 8px 16px;
  background: #2196f3;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>