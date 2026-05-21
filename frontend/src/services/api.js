/**
 * API сервис для взаимодействия с backend.
 * Централизует все HTTP запросы к FastAPI серверу.
 * Использует axios для выполнения запросов.
 */

import axios from 'axios'

// URL бэкенда на Render
const API_BASE_URL = 'https://fastapi-backend-6crk.onrender.com/api'

// Создаем экземпляр axios с увеличенным таймаутом (Render free tier засыпает)
const apiClient = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
    timeout: 30000, // 30 секунд — Render может долго просыпаться
})

// Retry логика: если запрос упал — пробуем ещё раз
apiClient.interceptors.response.use(
    (response) => response,
    async (error) => {
        const config = error.config
        if (!config || config.__retryCount >= 2) {
            return Promise.reject(error)
        }
        config.__retryCount = (config.__retryCount || 0) + 1
        // Ждём 2 секунды перед повтором
        await new Promise((resolve) => setTimeout(resolve, 2000))
        return apiClient(config)
    },
)

export const productsAPI = {
    getAll() {
        return apiClient.get('/products')
    },
    getById(id) {
        return apiClient.get(`/products/${id}`)
    },
    getByCategory(categoryId) {
        return apiClient.get(`/products/category/${categoryId}`)
    },
}

export const categoriesAPI = {
    getAll() {
        return apiClient.get('/categories')
    },
    getById(id) {
        return apiClient.get(`/categories/${id}`)
    },
}

export const cartAPI = {
    addItem(item, cartData) {
        return apiClient.post('/cart/add', {
            product_id: item.product_id,
            quantity: item.quantity,
            cart: cartData,
        })
    },
    getCart(cartData) {
        return apiClient.post('/cart', cartData)
    },
    updateItem(item, cartData) {
        return apiClient.put('/cart/update', {
            product_id: item.product_id,
            quantity: item.quantity,
            cart: cartData,
        })
    },
    removeItem(productId, cartData) {
        return apiClient.delete(`/cart/remove/${productId}`, {
            data: { cart: cartData },
        })
    },
}

export default apiClient
