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

4. **Run Locally:**
   ```bash
   python azad_website/manage.py makemigrations
   python azad_website/manage.py migrate
   python azad_website/manage.py runserver

5. **Run Docker (Optional):**
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

   Discover the Heartbeat of Azad Hall through Vibrant Events!

   Stay tuned for a diverse range of events that bring our community together. From cultural extravaganzas to tech hackathons, we celebrate the spirit of unity and collaboration. Join us in creating memories that last a lifetime!



## Technologies Used

- **Django Framework:** The web application is developed using the Django framework, providing a robust and scalable structure.

- **SQL:** Structured Query Language is used for managing the database, ensuring data integrity and efficient retrieval.

- **Nginx:** Nginx is used as a web server to handle incoming HTTP requests efficiently.

- **Gunicorn:** Gunicorn serves as the WSGI server to run the Django application in production.

- **Docker:** Docker containers are employed for easy deployment and management of the application.

## Upcoming Features

- [ ] **Blog System**
   - Explore and Share Stories with Our Upcoming Blog System!

- [ ] **Event (Upcoming Features)**
   -  New Event Update Notification: Receive instant notifications for upcoming events! Stay informed and never miss a moment with our event update notifications.
   -  Event Highlights: Introducing event highlights, showcasing memorable moments, participant achievements, and the vibrant energy that defines Azad Hall events.



## About Azad Hall

   Welcome to Azad Hall - Where Traditions Meet Innovation!

   Nestled in the heart of our vibrant campus, Azad Hall is more than just a residence; it's a tapestry of stories, a hub of creativity, and a home where lifelong friendships are forged. Explore our history, embrace our facilities, and become part of a community that thrives on diversity and excellence.

   Here, we blend the legacy of our past with the energy of the present, creating an environment where every individual contributes to the collective brilliance of Azad Hall. Join us on a journey where every day is an opportunity to learn, grow, and make a lasting impact!


## Team Members

Meet the dedicated individuals working behind the scenes to make the Azad Hall website a success:

- **[Harsh Gupta](https://github.com/dudegladiator)**
  - *Role:* Hosting, Back-end and Database

- **[Harsh Vardhan Gupta](https://github.com/harshvg247)**
  - *Role:* Front-end and Back-end

<!-- Add more team members as needed -->




