# HRMS Lite – Backend

##  Project Overview
HRMS Lite is a lightweight Human Resource Management System that provides RESTful APIs for:

- Managing employee records (Add, List, Delete)
- Marking and viewing employee attendance

This backend is built using Django and uses MongoDB as the primary database. It is deployed on Render and serves as the API layer for the React frontend.

---

##  Tech Stack

**Backend:**
- Python 3.10+
- Django 6.0.1
- Django REST Framework
- Gunicorn (Production server)

**Database:**
- MongoDB (MongoDB Atlas)

**Deployment:**
- Render

---

## Live Backend URL Get All Employees Method GET
https://backendhrms-egbi.onrender.com/api/employees/  


## -Post Employees
POST /api/employees/add/

## - Delete employee:  
DELETE /api/employees/<employee_id>/

## - Mark attendance:  
POST /api/attendance/mark/

##  - View attendance:  
GET /api/attendance/<employee_id>/



### 1 - Clone the repository
git clone https://github.com/sharmaprinceji/backendHrms.git
cd hrms-lite/backendHrms


## 2 - Create virtual environment
python -m venv venv

## 3 - Windows: venv\Scripts\activate
     - Mac/Linux:source venv/bin/activate

## 4 - Install dependencies
pip install -r requirements.txt

## 5 - .env file in backend root
SECRET_KEY=your_random_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/hrms-lite

## 6 - Run the server
python manage.py runserver

Backend will be available at:http://127.0.0.1:8000/
