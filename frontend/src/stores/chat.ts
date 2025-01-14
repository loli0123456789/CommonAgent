import { defineStore } from "pinia";
import { ref } from "vue";
import { chatService } from "@/services/api";

interface ChatResponse {
  response: string;
  conversation_id?: string;
}

export const useChatStore = defineStore("chat", () => {
  const conversationId = ref<string | null>(null);
  
  const sendMessage = async (message: string): Promise<ChatResponse> => {
    try {
      const response = await chatService.chat(
        message,
        conversationId.value || "",
        "zhipu"
      );
      return response.data;
    } catch (error) {
      console.error("发送消息失败：", error);
      throw error;
    }
  };

  return {
    sendMessage,
  };
});