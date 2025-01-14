import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useLayoutStore = defineStore('layout', () => {
  const isMenuOpen = ref(true)
  const isMobile = ref(false)

  const toggleMenu = () => {
    isMenuOpen.value = !isMenuOpen.value
  }

  const checkMobile = () => {
    isMobile.value = window.innerWidth <= 768
    // 移动端默认收起，PC端默认展开
    isMenuOpen.value = !isMobile.value
  }

  return {
    isMenuOpen,
    isMobile,
    toggleMenu,
    checkMobile
  }
})