# Content Platform

This is a Django-based content platform that allows users to create, read, update, and delete articles. The project also includes RESTful APIs for interacting with the articles.

## Features

- List all articles
- View details of a specific article
- Create a new article
- Update an existing article
- Delete an article
- RESTful API for articles

## Technologies Used

- Django
- Django REST framework
- PostgreSQL

## Prerequisites

- Python 3.6+
- PostgreSQL

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vismayparekh/content-platform.git
   cd content-platform

2. Create and activate a virtual environment:
     python3 -m venv venv
     source venv/bin/activate
   
3. Configure the PostgreSQL database:
     Ensure PostgreSQL is installed and running.
     Create a database named Content_Platform.
     Update the DATABASES settings in settings.py with your PostgreSQL credentials.
   
4. Apply the migrations:
     python manage.py migrate

5. Run the development server:
     python manage.py runserver



