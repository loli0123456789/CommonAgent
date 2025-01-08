import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json'
  }
});

// 用户相关API
export const authService = {
  register: (username: string, email: string, password: string) => 
    api.post('/register', { username, email, password }),
  
  login: (username: string, password: string) =>
    api.post('/login', { username, password })
};

export const userService = {
  getUsers: () => api.get('/users/').then(res => res.data.data)
};

export default api;
