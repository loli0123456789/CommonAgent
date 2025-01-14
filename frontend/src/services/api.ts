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
  chat: (message: string, conversation_id: string,model:string) =>
    api.post('/chat', { message, conversation_id,model })
};

export default api;
