from rest_framework.response import Response
from rest_framework.decorators import api_view
from .db import db
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

@api_view(["POST"])
def add_employee(request):
    data = request.data

    required_fields = ["employee_id", "full_name", "email", "department"]

    for field in required_fields:
        if not data.get(field):
            return Response({"error": f"{field} is required"}, status=400)

    if not is_valid_email(data["email"]):
        return Response({"error": "Invalid email format"}, status=400)

    if db.employees.find_one({"employee_id": data["employee_id"]}):
        return Response({"error": "Employee ID already exists"}, status=400)

    db.employees.insert_one(data)
    return Response({"message": "Employee added successfully"}, status=201)

@api_view(["GET"])
def list_employees(request):
    employees = list(db.employees.find({}, {"_id": 0}))
    return Response(employees)

@api_view(["DELETE"])
def delete_employee(request, emp_id):
    result = db.employees.delete_one({"employee_id": emp_id})

    if result.deleted_count == 0:
        return Response({"error": "Employee not found"}, status=404)

    return Response({"message": "Employee deleted"})

@api_view(["POST"])
def mark_attendance(request):
    data = request.data

    required_fields = ["employee_id", "date", "status"]

    for field in required_fields:
        if not data.get(field):
            return Response({"error": f"{field} is required"}, status=400)

    if data["status"] not in ["Present", "Absent"]:
        return Response({"error": "Status must be Present or Absent"}, status=400)

    db.attendance.insert_one(data)
    return Response({"message": "Attendance marked"}, status=201)

@api_view(["GET"])
def get_attendance(request, emp_id):
    records = list(db.attendance.find({"employee_id": emp_id}, {"_id": 0}))
    return Response(records)
