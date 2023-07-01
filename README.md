# Django-Vue-Inertia

This repository is a practice project that demonstrates the integration of Django, Vue.js, and Inertia.js to create a full-stack web application.
This project serves as a hands-on practice exercise for integrating Django, a powerful Python web framework, with Vue.js, a popular JavaScript framework, using Inertia.js, a modern framework-agnostic library.
By combining the strengths of Django on the backend and Vue.js on the frontend, developers can build dynamic and responsive web applications with ease. Inertia.js simplifies the data flow between the server and the client, allowing for seamless communication and efficient rendering of components.

## Technologies Used

### Backend

- Python: The programming language used for the backend development.
- Django: A powerful web framework for building web applications with Python.

### Frontend

- Vue.js: A JavaScript framework for building user interfaces.
- Vite: A fast and lightweight development server for Vue.js applications.

### Middleware

- Inertia.js: A framework-agnostic library that enables server-driven single-page applications.

Inertia.js middleware is used to seamlessly communicate between the Django backend and the Vue.js frontend, allowing for efficient rendering and data flow.

### Database

- SQLite: A lightweight and file-based relational database used for data storage.

## Getting Started

To set up the project locally, follow these steps:

1. Clone the repository
2. Navigate to the project directory: `cd Django_Inertia_Vue`
3. Set up the backend:

   - Create a virtual environment named `venv`:

     ```
     python -m venv venv
     ```

   - Activate the virtual environment:

     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```
       source venv/bin/activate
       ```

   - Install the required Python packages:

     ```
     pip install -r requirements.txt
     ```

   - Apply database migrations:

     ```
     python manage.py migrate
     ```

   - Start the Django development server:
     ```
     python manage.py runserver
     ```

4. Set up the Frontend:

   - Install the frontend dependencies:

     ```
     npm install
     ```

   - Start the Vue development server:

     ```
     npm run dev
     ```

5. Access the application by visiting `http://localhost:8000` in your web browser.
