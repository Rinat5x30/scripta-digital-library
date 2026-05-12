# Scripta - Digital Library Platform

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0+-green?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

**Scripta** is a modern digital library platform built with Django. It provides a clean interface for browsing, searching, and managing a collection of e-books.

## Features

- **Book Catalog** — Full-featured catalog with filtering by genre, language, and rating
- **Search** — Fast search by title and author
- **Rating System** — Rate books and view reviews
- **Dark Mode** — Light and dark theme support
- **Multilingual** — Russian and English language support
- **Responsive Design** — Optimized for mobile devices
- **PDF Reader** — Built-in PDF viewer
- **Feedback System** — Form for submitting feedback and suggestions
- **Modern UI** — Clean and intuitive interface with CSS variables

## Tech Stack

### Backend
- **Framework**: Django 4.0+
- **Database**: SQLite (development), PostgreSQL (production)
- **Web Server**: Gunicorn
- **Static Files**: WhiteNoise
- **CORS**: django-cors-headers

### Frontend
- **HTML5** & **CSS3** with theming variables
- **Vanilla JavaScript** for interactivity
- **Responsive Design** with mobile-first approach

### Deployment
- **Railway** / **Render** (cloud hosting)
- **GitHub Actions** (CI/CD)

## Requirements

- Python 3.9+
- pip
- Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rinat5x30/scripta-digital-library.git
cd scripta-digital-library
```

### 2. Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env`:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOW_ALL_ORIGINS=True
DATABASE_URL=sqlite:///db.sqlite3
```

> **Note**: Never commit the `.env` file to Git. Use environment variables on servers.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

The app will be available at `http://localhost:8000`

## Project Structure

```
scripta/
├── main/                      # Main Django application
│   ├── migrations/            # Database migrations
│   ├── static/
│   │   └── main/
│   │       ├── css/           # Styles (styles.css)
│   │       ├── js/            # JavaScript (book.js, main.js, lang.js, theme.js)
│   │       ├── img/           # Images
│   │       └── fonts/         # Custom fonts
│   ├── templates/
│   │   └── main/              # HTML templates
│   ├── models.py              # Data models (Book, Feedback)
│   ├── views.py               # Views
│   ├── urls.py                # URL routes
│   ├── forms.py               # Django forms
│   └── admin.py               # Admin configuration
├── scripta/                   # Django project configuration
│   ├── settings.py            # Settings
│   ├── urls.py                # URL configuration
│   ├── wsgi.py                # WSGI configuration
│   └── asgi.py                # ASGI configuration
├── media/                     # Uploaded files (covers, PDFs)
├── manage.py                  # Django management
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (git ignored)
├── .gitignore                 # Git ignore
├── Procfile                   # Heroku/Railway configuration
└── README.md                  # This file
```

## Data Models

### Book
```python
- title: CharField
- author: CharField
- published_date: PositiveIntegerField
- genre: CharField
- language: CharField
- pages: PositiveIntegerField
- description: TextField
- rating: FloatField
- cover_image: ImageField
- pdf_file: FileField
- status: CharField (regular, new, recommended, best)
```

### Feedback
```python
- user_name: CharField
- email: EmailField
- comment: TextField
- created_at: DateTimeField
```

## Security

- **SECRET_KEY** stored in environment variables
- **DEBUG** disabled in production
- **CSRF Protection** enabled
- **CORS** configured securely
- **HTTPS** recommended for production
- **Security Headers** configured (X-Frame-Options, etc.)
- **SQL Injection** protection via ORM
- **XSS** protection built into Django

### Security variables in `.env`:

```env
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
```

## Deployment

### Railway

1. Connect your GitHub repository to Railway
2. Add environment variables in the Railway Dashboard
3. Deploy

### Render

1. Create a new Web Service on Render
2. Point to your GitHub repository
3. Set environment variables
4. Deploy

## Testing

```bash
# Run tests
python manage.py test

# With coverage
coverage run --source='.' manage.py test
coverage report
```

## Migrations

```bash
# Create a new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

## Customization

### Change color scheme

Edit CSS variables in `main/static/main/css/styles.css`:

```css
:root {
    --primary-color: #5b21b6;
    --primary-hover: #4c1d95;
    --accent-color: #7c3aed;
    /* other variables */
}
```

### Add a new language

Edit `main/static/main/js/lang.js` and add a new language:

```javascript
const translations = {
    'en': { /* translations */ },
    'ru': { /* translations */ },
    'es': { /* add new language */ }
};
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Made with love by Rinat**
