Вот твоя проблема! В template написано буквально `...` вместо компонентов. Замени весь файл на это:

```vue
<template>
    <div class="min-h-screen bg-gray-50">
        <Header />
        <router-view />
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import Header from '@/components/Header.vue'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()

onMounted(() => {
    cartStore.initCart()
})
</script>
```

Пушь и всё заработает 🎉
