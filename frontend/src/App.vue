<<<<<<< HEAD
Вот твоя проблема! В template написано буквально `...` вместо компонентов. Замени весь файл на это:

```vue
<template>
    <div class="min-h-screen bg-gray-50">
        <Header />
        <router-view />
    </div>
=======
<template>
  <div class="min-h-screen bg-gray-50">
    <Header />
    <router-view />
  </div>
>>>>>>> 0cd2938f2709993d97ce641564cf811ee8b877a0
</template>

<script setup>
import { onMounted } from 'vue'
import Header from '@/components/Header.vue'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()

onMounted(() => {
<<<<<<< HEAD
    cartStore.initCart()
})
</script>
```

Пушь и всё заработает 🎉
=======
  cartStore.initCart()
})
</script>
>>>>>>> 0cd2938f2709993d97ce641564cf811ee8b877a0
