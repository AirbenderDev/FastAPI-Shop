# 🛍️ FastAPI Shop

> Fullstack e-commerce приложение с FastAPI бэкендом и Vue.js фронтендом

[![FastAPI](https://img.shields.io/badge/FastAPI-0.136.1-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.5.32-4FC08D?style=for-the-badge&logo=vue.js)](https://vuejs.org/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://python.org/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind-4.3.0-38B2AC?style=for-the-badge&logo=tailwind-css)](https://tailwindcss.com/)

🌐 **Live Demo:** [frontend-fastapi.vercel.app](https://frontend-fastapi-593elsl7d-airbenderdevs-projects.vercel.app/)
🔗 **API Docs:** [fastapi-backend-6crk.onrender.com/api/docs](https://fastapi-backend-6crk.onrender.com/api/docs)

---

## ✨ Возможности

- 📦 Каталог товаров с фильтрацией по категориям
- 🛒 Корзина с возможностью изменения количества
- 🔍 Детальная страница каждого товара
- 📱 Полностью адаптивный дизайн
- ⚡ REST API с автодокументацией Swagger

---

## 🏗️ Стек технологий

### Backend
| Технология | Версия | Описание |
|---|---|---|
| Python | 3.11 | Основной язык |
| FastAPI | 0.136.1 | Веб-фреймворк |
| SQLAlchemy | 2.0.49 | ORM |
| Pydantic | 2.13.4 | Валидация данных |
| Uvicorn | 0.47.0 | ASGI сервер |
| SQLite | — | База данных |

### Frontend
| Технология | Версия | Описание |
|---|---|---|
| Vue.js | 3.5.32 | UI фреймворк |
| Vue Router | 5.0.4 | Маршрутизация |
| Pinia | 3.0.4 | State management |
| Axios | 1.16.1 | HTTP клиент |
| Tailwind CSS | 4.3.0 | Стилизация |
| Vite | 8.0.8 | Сборщик |

### Деплой
| Сервис | Назначение |
|---|---|
| [Render](https://render.com) | Хостинг бэкенда |
| [Vercel](https://vercel.com) | Хостинг фронтенда |

---

## 🚀 Быстрый старт

### Требования
- Python 3.11+
- Node.js 20+

### 1. Клонировать репозиторий
```bash
git clone https://github.com/AirbenderDev/FastAPI-Shop.git
cd FastAPI-Shop
```

### 2. Запустить бэкенд
```bash
cd backend
pip install -r requirements.txt
python seed_data.py      # Заполнить БД тестовыми данными
python run.py            # Запустить сервер
```
Бэкенд будет доступен на `http://localhost:8000`

### 3. Запустить фронтенд
```bash
cd frontend
npm install
npm run dev
```
Фронтенд будет доступен на `http://localhost:5173`

---

## 📁 Структура проекта

```
FastAPI-Shop/
├── backend/
│   ├── app/
│   │   ├── models/          # SQLAlchemy модели
│   │   ├── schemas/         # Pydantic схемы
│   │   ├── repositories/    # Работа с БД
│   │   ├── services/        # Бизнес-логика
│   │   ├── routes/          # API эндпоинты
│   │   ├── database.py      # Подключение к БД
│   │   ├── config.py        # Конфигурация
│   │   └── main.py          # Точка входа
│   ├── seed_data.py         # Тестовые данные
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── components/      # Vue компоненты
│   │   ├── views/           # Страницы
│   │   ├── stores/          # Pinia stores
│   │   ├── services/        # API сервисы
│   │   ├── router/          # Маршруты
│   │   └── main.js
│   ├── package.json
│   └── Dockerfile
│
└── docker-compose.yml
```

---

## 🔌 API Endpoints

| Метод | Эндпоинт | Описание |
|---|---|---|
| `GET` | `/api/products` | Все товары |
| `GET` | `/api/products/{id}` | Товар по ID |
| `GET` | `/api/products/category/{id}` | Товары по категории |
| `GET` | `/api/categories` | Все категории |
| `POST` | `/api/cart` | Получить корзину |
| `POST` | `/api/cart/add` | Добавить в корзину |
| `PUT` | `/api/cart/update` | Обновить количество |
| `DELETE` | `/api/cart/remove/{id}` | Удалить из корзины |

Полная документация: `/api/docs` (Swagger UI)

---

## 🐳 Docker

```bash
docker-compose up --build
```

---

## 👨‍💻 Автор

**AirbenderDev** — [@AirbenderDev](https://github.com/AirbenderDev)

---

<p align="center">Сделано с ❤️ и большим количеством кофе</p>
