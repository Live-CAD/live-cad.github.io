export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      apiBase: 'http://localhost:8000', // Backend API URL
    },
  },

  
  pages: false,
  compatibilityDate: '2025-01-09'
})