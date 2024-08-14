# Blog API with JWT Authentication

This project is a fully functional Blog API built with Django Rest Framework (DRF) that includes JWT (JSON Web Token) authentication. It features a custom user model with email as the unique identifier, allowing users to create, manage, and interact with blog posts and comments securely.

## Features

- **Custom User Model**: Utilizes a custom user model where the email is the primary identifier.
- **JWT-Based Authentication**: Secure token-based authentication for managing user sessions.
- **Post Management**: Create, retrieve, update, and delete blog posts.
- **Like/Dislike Feature**: Users can like or dislike posts, with tracking for each post.
- **Commenting System**: Users can add, retrieve, and manage comments on posts, with support for threaded discussions.

## Technologies Used

- **Django**: Web framework for backend development.
- **Django Rest Framework**: For building RESTful APIs.
- **JWT (JSON Web Tokens)**: For secure authentication and session management.
- **PostgreSQL/MySQL**: Database options for storing user, post, and comment data.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/blog-api.git
   cd blog-api
## Create and Activate a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
## Install Dependencies:
pip install -r requirements.txt
## Apply Migrations:
python manage.py migrate
## Create a Superuser (for admin access):
python manage.py createsuperuser
## Run the Development Server:
python manage.py runserver
## Usage
# Authentication
# 1.Register:
POST /api/auth/register/
# 2.Login:
POST /api/auth/login/
# Post Management:
## 1.Retrieve All Posts:
GET /api/posts/
## 2.Create a Post:
POST /api/posts/
## 3.Retrieve a Specific Post:
GET /api/posts/{id}/
## 4.Update a Post:
PUT /api/posts/{id}/
## 5.Delete a Post:
DELETE /api/posts/{id}/
## Like/Dislike
## *Like/Dislike a Post:
POST /api/posts/{id}/like/
## Commenting
## 1.Add a Comment:
POST /api/posts/{id}/comments/
## 2.Retrieve Comments for a Post:
GET /api/posts/{id}/comments/
## Security
JWT Expiry and Refresh: Tokens have a limited lifespan and can be refreshed.
Password Hashing: Passwords are securely hashed.
Rate Limiting: Applied to sensitive endpoints.
Access Control: Ensures authenticated access to protected resources.
## Contact
For any questions or feedback, please contact email ayush952877@gmail.com.
