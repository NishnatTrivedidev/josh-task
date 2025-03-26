# Task Management API

This is a Django REST Framework (DRF) based API for managing tasks and user assignments.

## Features
- Create tasks
- Assign tasks to multiple users
- Fetch tasks assigned to a specific user
- Create new users
- Fetch all users

## Installation

### Prerequisites
Ensure you have Python 3.8+ and `pip` installed.

### Steps
1. Clone the repository:
   git clone <repository_url>
   cd <project_directory>
   
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. Install dependencies:
   pip install -r requirements.txt
  
4. Apply migrations:
   python manage.py migrate
   
5. Start the development server:
   python manage.py runserver
   

## API Endpoints

### Create Task -POST
curl --location 'http://127.0.0.1:8000/api/tasks/create/' \
--header 'Content-Type: application/json' \
--data '{
           "task_id": 1,
           "user_ids": [2, 3]
         }'


### Assign Task to Users-POST
curl --location 'http://127.0.0.1:8000/api/tasks/assign/' \
--header 'Content-Type: application/json' \
--data '{
           "task_id": 1,
           "user_ids": [2, 3]
         }'

### Get User Tasks - GET
**Endpoint:** `http://127.0.0.1:8000/api/tasks/user/userid

## Dependencies
See `requirements.txt` for required Python packages.


