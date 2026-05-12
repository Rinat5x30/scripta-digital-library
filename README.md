# 📚 Scripta - Digital Library Platform

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0+-green?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

**Scripta** — это современная платформа цифровой библиотеки, разработанная на Django. Она предоставляет удобный интерфейс для просмотра, поиска и управления коллекцией электронных книг.

## 🌟 Основные возможности

- 📖 **Каталог книг** — Полнофункциональный каталог с фильтрацией по жанрам, языкам и рейтингу
- 🔍 **Поиск** — Быстрый поиск по названию и автору
- ⭐ **Рейтинговая система** — Оценка книг и просмотр отзывов
- 🌙 **Темная тема** — Поддержка светлой и темной темы интерфейса
- 🌐 **Многоязычность** — Поддержка русского и английского языков
- 📱 **Адаптивный дизайн** — Оптимизирован для мобильных устройств
- 📕 **PDF Читатель** — Встроенный просмотр PDF-документов
- 💬 **Система обратной связи** — Форма для отправки отзывов и предложений
- 🎨 **Современный UI** — Красивый и интуитивный интерфейс с CSS переменными

## 🛠 Технологический стек

### Backend
- **Framework**: Django 4.0+
- **Database**: SQLite (development), PostgreSQL (production)
- **Web Server**: Gunicorn
- **Static Files**: WhiteNoise
- **CORS**: django-cors-headers

### Frontend
- **HTML5** & **CSS3** с переменными для теминга
- **Vanilla JavaScript** для интерактивности
- **Responsive Design** с mobile-first подходом

### Deployment
- **Railway** / **Render** (cloud hosting)
- **GitHub Actions** (CI/CD)

## 📋 Требования

- Python 3.9+
- pip или poetry
- Git

## 🚀 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/scripta.git
cd scripta
```

### 2. Создание виртуального окружения

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Конфигурация переменных окружения

Создайте файл `.env` в корневой папке проекта:

```bash
cp .env.example .env
```

Отредактируйте `.env`:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOW_ALL_ORIGINS=True
DATABASE_URL=sqlite:///db.sqlite3
```

> ⚠️ **Важно**: Никогда не коммитьте файл `.env` в Git. Используйте переменные окружения на серверах.

### 5. Миграции базы данных

```bash
python manage.py migrate
```

### 6. Создание суперпользователя (опционально)

```bash
python manage.py createsuperuser
```

### 7. Запуск сервера разработки

```bash
python manage.py runserver
```

Приложение будет доступно по адресу: `http://localhost:8000`

## 📁 Структура проекта

```
scripta/
├── main/                      # Основное Django приложение
│   ├── migrations/           # Миграции БД
│   ├── static/
│   │   └── main/
│   │       ├── css/          # Стили (styles.css)
│   │       ├── js/           # JavaScript (book.js, main.js, lang.js, theme.js)
│   │       ├── img/          # Изображения
│   │       └── fonts/        # Кастомные шрифты
│   ├── templates/
│   │   └── main/             # HTML шаблоны
│   ├── models.py             # Модели данных (Book, Feedback)
│   ├── views.py              # Представления
│   ├── urls.py               # URL маршруты
│   ├── forms.py              # Django формы
│   └── admin.py              # Администрирование
├── scripta/                   # Конфигурация Django проекта
│   ├── settings.py           # Основные настройки
│   ├── urls.py               # URL конфигурация
│   ├── wsgi.py               # WSGI конфигурация
│   └── asgi.py               # ASGI конфигурация
├── media/                    # Загруженные файлы (обложки, PDF)
├── manage.py                 # Django управление проектом
├── requirements.txt          # Зависимости Python
├── .env                      # Переменные окружения (git ignore)
├── .gitignore               # Git ignore файл
├── Procfile                 # Конфигурация для Heroku/Railway
└── README.md                # Этот файл
```

## 🗄️ Модели данных

### Book
```python
- title: CharField (название)
- author: CharField (автор)
- published_date: PositiveIntegerField (год)
- genre: CharField (жанр)
- language: CharField (язык)
- pages: PositiveIntegerField (количество страниц)
- description: TextField (описание)
- rating: FloatField (рейтинг)
- cover_image: ImageField (обложка)
- pdf_file: FileField (PDF файл)
- status: CharField (статус: regular, new, recommended, best)
```

### Feedback
```python
- user_name: CharField (имя пользователя)
- email: EmailField (почта)
- comment: TextField (комментарий)
- created_at: DateTimeField (дата создания)
```

## 🔐 Безопасность

Проект следует лучшим практикам безопасности Django:

- ✅ **SECRET_KEY** хранится в переменных окружения
- ✅ **DEBUG** отключен в продакшене
- ✅ **CSRF Protection** включена
- ✅ **CORS** настроена безопасно
- ✅ **HTTPS** рекомендуется для продакшена
- ✅ **Security Headers** настроены (X-Frame-Options, etc.)
- ✅ **SQL Injection** защита через ORM
- ✅ **XSS** защита встроена в Django

### Переменные безопасности в .env:

```env
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
```

## 📦 Развертывание

### Railway

1. Свяжите репозиторий GitHub с Railway
2. Добавьте переменные окружения в Railway Dashboard
3. Разверните приложение

### Render

1. Создайте новый Web Service на Render
2. Укажите GitHub репозиторий
3. Установите переменные окружения
4. Разверните

## 🧪 Тестирование

```bash
# Запуск тестов
python manage.py test

# С покрытием
coverage run --source='.' manage.py test
coverage report
```

## 📝 Миграция данных

```bash
# Создание новой миграции
python manage.py makemigrations

# Применение миграций
python manage.py migrate
```

## 🎨 Кастомизация

### Изменение цветовой схемы

Отредактируйте CSS переменные в `main/static/main/css/styles.css`:

```css
:root {
    --primary-color: #5b21b6;
    --primary-hover: #4c1d95;
    --accent-color: #7c3aed;
    /* и другие переменные */
}
```

### Добавление нового языка

Отредактируйте `main/static/main/js/lang.js` и добавьте новый язык:

```javascript
const translations = {
    'en': { /* переводы */ },
    'ru': { /* переводы */ },
    'es': { /* добавьте новый язык */ }
};
```

## 🐛 Отладка

```bash
# Запуск с отладкой
python manage.py runserver --verbosity 3

# Django shell
python manage.py shell

# Просмотр журнала
tail -f debug.log
```

## 📞 Поддержка и контакты

- 📧 **Email**: support@scripta.com
- 🌐 **Website**: https://scripta.app
- 💬 **Issues**: Используйте GitHub Issues для отчетов об ошибках

## 📄 Лицензия

Этот проект лицензирован под лицензией MIT. Смотрите файл [LICENSE](LICENSE) для деталей.

## 🙏 Благодарности

Спасибо всем, кто способствовал развитию этого проекта!

---

**Made with ❤️ by Scripta Team**

**Последнее обновление**: 12 мая 2026 г.
