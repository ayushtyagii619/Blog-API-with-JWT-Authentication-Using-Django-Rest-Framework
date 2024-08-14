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
