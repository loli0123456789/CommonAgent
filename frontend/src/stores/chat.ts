import { defineStore } from "pinia";
import { ref } from "vue";
import { chatService } from "@/services/api";

interface ChatResponse {
  response: string | AsyncIterable<string>;
  conversation_id?: string;
}

export const useChatStore = defineStore("chat", () => {
  const conversationId = ref<string | null>(null);
  
  const sendMessage = (message: string): AsyncIterable<string> => {
    return chatService.chat(
      message,
      conversationId.value || "",
      "zhipu"
    );
  };

  return {
    sendMessage,
    conversationId
  };
});