# First Full-Stack App 🎉

Welcome to my first full-stack web application! 🚀  

## 🌍 Live Demo  
🔗 Check out the live version of the app here:  
[Click to Visit](https://firstfullstackapp-myta.onrender.com/)

## 📖 About  
This is my first deployed full-stack web application, built with Django and hosted on Render.  

## ⚙️ Technologies Used  
- **Django** (Backend)  
- **HTML, CSS, JavaScript** (Frontend)  
- **Render** (Deployment)  
- **PostgreSQL** (Database)

## 💻 Local Setup & Commands

Follow these steps to set up the project locally:

1. **Create a Project Folder**  
   - Create a new folder for your project.

2. **Open Terminal in the Project Folder**  
   - Navigate to your project destination folder and open the terminal.

3. **Check Python Installation**  
   - Verify that Python is installed by running:
     ```bash
     python --version
     ```

4. **Create a Virtual Environment**  
   - Create a virtual environment with:
     ```bash
     python -m venv venv
     ```

5. **Activate the Virtual Environment**  
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

6. **Install Django**  
   - Install Django within the virtual environment:
     ```bash
     pip install django
     ```
     *Or alternatively:*
     ```bash
     python -m pip install django
     ```

7. **Check Django Version**  
   - Verify Django is installed:
     ```bash
     django-admin --version
     ```
     *Or:*
     ```bash
     python -m django --version
     ```

8. **Start a New Django Project**  
   - Create a new project named `backend`:
     ```bash
     django-admin startproject backend
     ```
     *If you get a `CommandNotFoundException`, try:*
     ```bash
     python -m django startproject backend
     ```
     *then run:*
     ```bash
     django-admin startproject backend
     ```

9. **Open the Project in Visual Studio Code**  
   - Open your project with:
     ```bash
     code .
     ```

10. **Navigate to the Project Folder**  
    - Change directory to the new project folder:
      ```bash
      cd backend
      ```

11. **Run the Development Server**  
    - Start the server:
      ```bash
      python manage.py runserver
      ```
    - Access the development server at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
    - Press `Ctrl+C` to stop the server.

12. **Apply Migrations**  
    - Connect Django to the database and apply initial migrations:
      ```bash
      python manage.py migrate
      ```

13. **Run the Server Again**  
    - Restart the server:
      ```bash
      python manage.py runserver
      ```
    - Verify that migrations for `admin`, `auth`, `contenttypes`, and `sessions` are applied by checking [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

14. **Create a New App**  
    - Start a new Django app named `core`:
      ```bash
      python manage.py startapp core
      ```

15. **Configure the New App**  
    - In Visual Studio Code, open the `settings.py` file located in the `backend` folder.
    - Add `'core'` to the `INSTALLED_APPS` list.

16. **Make Migrations for the New App**  
    - Create migrations for your app:
      ```bash
      python manage.py makemigrations
      ```
    - Apply the migrations:
      ```bash
      python manage.py migrate
      ```

17. **Create a Superuser**  
    - Create an admin user:
      ```bash
      python manage.py createsuperuser
      ```

18. **Final Server Run**  
    - Run the server one more time:
      ```bash
      python manage.py runserver
      ```

Happy coding! 🚀
