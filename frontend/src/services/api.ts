import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.DEV
    ? import.meta.env.VITE_DEV_API_URL
    : import.meta.env.VITE_PROD_API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

// 调试日志
console.log('API baseURL:', api.defaults.baseURL);

// 用户相关API
export const authService = {
  register: (username: string, email: string, password: string) => 
    api.post('/users/register', { username, email, password }),
  
  login: (username: string, password: string) =>
    api.post('/users/login', { username, password })
};

export const userService = {
  getUsers: () => api.get('/users').then(res => res.data.data)
};

export const chatService = {
  chat: async function* (message: string, conversationId: string, model: string) {
    const response = await fetch(`${api.defaults.baseURL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message,
        conversation_id: conversationId,
        model
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const reader = response.body?.getReader();
    if (!reader) {
      throw new Error('Failed to get reader from response');
    }

    const decoder = new TextDecoder();
    let buffer = '';
    
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      
      buffer += decoder.decode(value, { stream: true });
      
      // Process complete SSE messages
      while (buffer.includes('\n\n')) {
        const messageEnd = buffer.indexOf('\n\n');
        const message = buffer.slice(0, messageEnd);
        buffer = buffer.slice(messageEnd + 2);
        
        if (message.startsWith('data: ')) {
          yield message.slice(6); // Remove 'data: ' prefix
        }
      }
    }
    
    // Process any remaining data
    if (buffer.startsWith('data: ')) {
      yield buffer.slice(6);
    }
  }
};

export default api;
