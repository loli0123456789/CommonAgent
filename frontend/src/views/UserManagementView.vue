<template>
  <div class="user-management">
    <h1>用户管理</h1>
    <table v-if="users.length > 0">
      <thead>
        <tr>
          <th>ID</th>
          <th>用户名</th>
          <th>邮箱</th>
          <th>注册时间</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>{{ formatDate(user.created_time) }}</td>
        </tr>
      </tbody>
    </table>
    <p v-else>加载中...</p>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { userService } from '../services/api';

interface User {
  id: number;
  username: string;
  email: string;
  created_time: string;
}

export default defineComponent({
  name: 'UserManagementView',
  setup() {
    const users = ref<User[]>([]);

    const fetchUsers = async () => {
      try {
        users.value = await userService.getUsers();
      } catch (error) {
        console.error('获取用户列表失败:', error);
        users.value = []; // 确保出错时也是空数组
      }
    };

    const formatDate = (dateString: string) => {
      return new Date(dateString).toLocaleString();
    };

    onMounted(() => {
      fetchUsers();
    });

    return {
      users,
      formatDate
    };
  }
});
</script>

<style scoped>
.user-management {
  padding: 0px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f5f5f5;
}
</style>
