# Azad Hall Website

## Overview

This repository contains the source code for the Azad Hall website, a platform designed to facilitate various services and provide information to the residents of Azad Hall. The website is built using the Django framework and utilizes Nginx, Docker, Gunicorn, and SQL to ensure a robust and scalable web application.

## Installation and Run

To set up the Azad Hall website locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dudegladiator/Azad-Hall-Website
   cd Azad-Hall-Website

2. **Create Virtual Env and Install all packages:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt

3. **Change Django Setting file**

4. Run Locally
   ```bash
   python azad_website/manage.py makemigrations
   python azad_website/manage.py migrate
   python azad_website/manage.py runserver

5. Run Docker (Optional)
   ```bash
   docker build --tag azad .
   docker run -p 8000:8000 azad

## Features

### Complaints

Residents can submit complaints related to mess services and maintenance through the website. The system ensures efficient handling and resolution of reported issues.

### Library Book Issuance

Residents can use the platform to request the issuance of books from the Azad Hall library. The website keeps track of book availability and facilitates the borrowing process.

### Library Book Inventory

The website provides an updated list of all books available in the Azad Hall library, making it easy for residents to explore the collection.

### Event

Details about different Events

### About Azad Hall

This section provides general information about Azad Hall, including its history, facilities, and any other relevant details.

## Technologies Used

- **Django Framework:** The web application is developed using the Django framework, providing a robust and scalable structure.

- **SQL:** Structured Query Language is used for managing the database, ensuring data integrity and efficient retrieval.

- **Nginx:** Nginx is used as a web server to handle incoming HTTP requests efficiently.

- **Gunicorn:** Gunicorn serves as the WSGI server to run the Django application in production.

- **Docker:** Docker containers are employed for easy deployment and management of the application.






