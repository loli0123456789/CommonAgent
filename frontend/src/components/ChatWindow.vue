<template>
  <div class="chat-window">
    <div class="messages" ref="messagesContainer">
      <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.role]">
        {{ msg.content }}
      </div>
    </div>
    <div class="input-area">
      <input v-model="inputText" @keyup.enter="sendMessage" placeholder="输入消息..." :disabled="isLoading" />
      <button @click="sendMessage" :disabled="isLoading">
        <span v-if="!isLoading">发送</span>
        <div v-else class="loading-indicator"></div>
      </button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, nextTick, onMounted } from "vue"
import { useChatStore } from "@/stores/chat"

onMounted(() => {
  scrollToBottom()
})

interface Message {
  role: string
  content: string
}

const chatStore = useChatStore()
const inputText = ref("")
const messages = ref<Message[]>([])
const messagesContainer = ref<HTMLElement | null>(null)
const isLoading = ref(false)

const scrollToBottom = () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}
const sendMessage = async () => {
  if (!inputText.value.trim()) return
  
  // 添加用户消息
  messages.value = [...messages.value, {
    role: "user",
    content: inputText.value
  }]
  
  // 添加空的AI消息占位符
  messages.value = [...messages.value, {
    role: "assistant",
    content: ""
  }]
  const aiMessageIndex = messages.value.length - 1
  
  try {
    isLoading.value = true
    const responseStream = chatStore.sendMessage(inputText.value)
    
    for await (const chunk of responseStream) {
      // 创建新消息对象强制触发更新
      // const newMessages = messages.value.map((msg, index) =>
      //   index === aiMessageIndex
      //     ? { ...msg, content: msg.content + chunk }
      //     : msg
      // )
      // messages.value = newMessages

      messages.value[aiMessageIndex].content += chunk

      scrollToBottom()

      // 在 for await 循环中添加
      await new Promise(resolve => setTimeout(resolve, 20)) // 通过延迟解决流式输出
    }
  } catch (error) {
    console.error("发送消息失败：", error)
    messages.value = [...messages.value, {
      role: "system",
      content: "消息发送失败，请稍后重试"
    }]
  }
  
  inputText.value = ""
  isLoading.value = false
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
  padding-bottom: 20px;
  scroll-behavior: smooth;
}

.message {
  margin: 4px 0;
  padding: 6px 10px;
  border-radius: 8px;
  max-width: 80%;
  white-space: pre-wrap;
}

.message.user {
  background: #e3f2fd;
  margin-left: auto;
  position: relative;
}

.message.user::after {
  content: "";
  width: 8px;
  height: 16px;
  background: #e3f2fd;
  position: absolute;
  bottom: -8px;
  right: 10px;
  clip-path: polygon(0 0, 0% 100%, 100% 0);
}

.message.assistant {
  background: #f5f5f5;
  margin-right: auto;
  position: relative;
}

.message.assistant::after {
  content: "";
  width: 8px;
  height: 16px;
  background: #f5f5f5;
  position: absolute;
  bottom: -8px;
  left: 10px;
  clip-path: polygon(0 0, 100% 0, 100% 100%);
}

.input-area {
  display: flex;
  padding: 10px;
  border-top: 1px solid #eee;
  position: relative;
}

.loading-indicator {
  width: 20px;
  height: 20px;
  border: 2px solid #f3f3f3;
  border-top: 2px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto;
  position: relative;
  top: 10px;
}

@keyframes spin {
  0% { transform: translateY(-50%) rotate(0deg); }
  100% { transform: translateY(-50%) rotate(360deg); }
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
