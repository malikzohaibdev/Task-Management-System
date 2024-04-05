# Task Management System

This project implements a Task Management System that allows users to create, update, delete, and assign tasks. The system consists of a Django backend for the web application, FastAPI for the RESTful API, and Celery for asynchronous task processing.

## Installation

### Clone the repository:
git clone <repository_url>

### Install the dependencies:
pip install -r requirements.txt

## Running the Application

### Start the Django server:
python manage.py runserver

### Start the FastAPI server:
uvicorn fastapi_app.app.main:app --reload --port 5001

### Start Celery for asynchronous task processing:
celery -A config worker --loglevel=info


## Access the application at:
* Django: http://localhost:8000
* FastAPI: http://localhost:5001/docs


## User Authentication
* Users can register, login, and logout from the system.
* Django's built-in authentication system is used for user authentication.


## Task Management
* Users can create tasks with details such as title, description, due date, and priority (Low, Medium, High).
* Tasks are editable and deletable by the creator.
* Tasks can be assigned to other users.
* Users can view a list of tasks they have created or assigned to them.
* Tasks can be filtered based on status (Open, In Progress, Completed).


## API Integration
* A RESTful API is implemented using FastAPI for CRUD operations on tasks.
* API endpoints support JSON requests and responses.
* Endpoints are available for task creation, retrieval, updating, and deletion.


## Users (Django)
Three users are pre-created in the Django backend with the following credentials:
* Username: zubair, Password: P@ssword001
* Username: talha, Password: P@ssword001
* Username: idrees, Password: P@ssword001


## Asynchronous Task Processing
* Celery is used for asynchronous task processing.
* When a task is created or updated, an email notification is sent asynchronously to the assigned user about the task details.


## Django Endpoints

### Task List (GET)
### Endpoint: /tasks/
* Method: GET
* Response:
    Status Code: 200 OK
    Body: HTML page containing a list of tasks with details.

### Task Creation Form (GET)
### Endpoint: /tasks/create/
* Method: GET
* Response:
    Status Code: 200 OK
    Body: HTML form to create a new task.

### Task Update Form (GET)
### Endpoint: /tasks/update/{task_id}/
* Method: GET
* Response:
    Status Code: 200 OK
    Body: HTML form pre-filled with task details for updating.

### Task Creation (POST)
### Endpoint: /tasks/create/
* Method: POST
* Expected Payload:
* Form data containing:
    Title
    Description
    Due Date
    Priority
    Status
* Response:
    Status Code: 302 Found (Redirect to Task List)

### Task Update (POST)
### Endpoint: /tasks/update/{task_id}/
* Method: POST
* Expected Payload:
    Form data similar to the task creation form.
* Response:
    Status Code: 302 Found (Redirect to Task List)

### Task Deletion (POST)
### Endpoint: /tasks/delete/{task_id}/
* Method: POST
* Response:
    Status Code: 302 Found (Redirect to Task List)

## FastAPI Endpoints

### Task Creation (POST)
### Endpoint: /tasks/
* Expected Payload: JSON payload containing title, description, due date, priority, and status.
* Response: Task details JSON object.

### Task Retrieval (GET)
### Endpoint: /tasks/
* Response: List of tasks with details in JSON format.

### Task Update (PUT)
### Endpoint: /tasks/{task_id}
* Expected Payload: JSON payload similar to the task creation payload.
* Response: Updated task details JSON object.

### Task Deletion (DELETE)
### Endpoint: /tasks/{task_id}
* Response: No content.