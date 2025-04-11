# 🌾 Farmers' Marketplace

A Django-based web platform that connects farmers to consumers, streamlines product listings, and allows reviews and location-based browsing. This project is built with scalability in mind using Django best practices and will later be extended with a Django Rest Framework (DRF) API.

---

## 📁 Project Structure

farmers_marketplace/ ├── config/ # Project settings ├── core/ # Utility modules, shared services ├── users/ # User auth, registration, RBAC ├── products/ # Product and Category models ├── locations/ # Location models ├── reviews/ # Product reviews ├── templates/ # HTML templates ├── static/ # CSS, JS, images ├── manage.py
---

## 🚀 Features

- 🔒 JWT-based authentication
- 👥 Role-Based Access Control (RBAC) using Django Groups & Permissions
- 🌍 Location-based product filtering
- 🌾 Farmer profile with product listings
- 🛒 Product categorization and nested category support
- 📝 Product reviews and ratings
- 🧪 RESTful API (DRF integration in progress)

---

## ⚙️ Tech Stack

- **Backend**: Django
- **API**: Django Rest Framework (DRF)
- **Auth**: JWT via `djangorestframework-simplejwt` and TokenAuth
- **Database**: SQLite (default) | PostgreSQL (production-ready)
- **Frontend**: Django templates (for admin and minimal pages)
- **RBAC**: Django Groups and Permissions
- **Others**: Django Environ, RESTful routers, Custom Middleware

---

## 🧱 Core Apps

| App       | Purpose                             |
|-----------|-------------------------------------|
| `users`   | User registration, login, roles     |
| `products`| Farmer products & categories        |
| `locations`| Manage user/product location       |
| `reviews` | User reviews for products           |
| `core`    | Common utilities and helpers        |

---

## 🔑 User Roles

- **Farmer**: Can list and manage their own products
- **Consumer**: Can view products and leave reviews
- **Admin**: Manages users, reviews, and settings

---

## 🧪 API Overview

| Endpoint               | Method | Description                     |
|------------------------|--------|---------------------------------|
| `/api/users/register/`| POST   | User registration (w/ `is_farmer`) |
| `/api/users/login/`   | POST   | Login returns token & user data |
| `/api/users/login/`   | GET    | Simple message for GET test     |
| `/api/users/login-page/`| GET | Renders login HTML template     |
| `/api/products/`       | GET/POST | List or create products       |
| `/api/products/{id}/`  | GET/PUT/DELETE | Detail, update, delete  |

---

## 🔨 Setup & Installation

1. **Clone repo**

```bash
git clone https://github.com/yourusername/farmers-marketplace.git
cd farmers-marketplace
