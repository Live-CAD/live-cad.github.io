<template>
  <div>
    <div>
      <h1>LiveCAD Products</h1>
      <ul>
        <li v-for="product in products" :key="product.id">
          {{ product.name }} - {{ product.description }}
        </li>
      </ul>
    </div>
    <NuxtPage />
  </div>
</template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const products = ref([])
  
  onMounted(async () => {
    const response = await fetch(`${useRuntimeConfig().public.apiBase}/products`)
    products.value = await response.json()
  })
  </script>