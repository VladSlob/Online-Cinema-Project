# Online-Cinema-Project (Vladyslav Slobodian)

Project Description:

This web application serves as an online cinema platform, enabling users to browse, search, buy, and watch movies. Built with the FastAPI framework, the application uses SQLAlchemy for database management with PostgreSQL.

Features:
+ JWT authentication
+ User registration and login
+ Password reset functionality
+ User profile management
+ User roles (admin, user)
+ Movie management (CRUD operations for admins)
+ Movie search and filtering
+ Movie rating and review system
+ Cart management
+ Order management
+ Payment processing (using Stripe)
+ Email notifications

How to Run the Project:

To set up and run the Online Cinema API project on your local machine, follow these steps.

1. Clone the Repository:

First, clone the project repository from GitHub.
```
git https://github.com/VladSlob/Online-Cinema-Project
cd online-cinema
```

2. Create and Activate a Virtual Environment

We recommend using a virtual environment to keep project dependencies isolated.
```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install Dependencies with Poetry

This project uses Poetry to manage its dependencies. Install them using the following command:
```
# Install Poetry if not already installed
pip install poetry

# Install project dependencies
poetry install
```

4. Create a .env File

Create a .env file in the main project directory and add the following variables to it.

Enter your database connection details and other necessary configuration settings into the .env file.
```
copy .env.example .env
```

5. Run the Docker Compose
```
docker-compose -f docker-compose-local.yml up --build
```

6. Run this command to start the development server:
```
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

Access the Services:
Service	URL
API	http://localhost:8000
pgAdmin	http://localhost:3333 (Use .env credentials)
MailHog UI	http://localhost:8025 (SMTP testing)
MinIO Console	http://localhost:9001 (S3-compatible storage)
