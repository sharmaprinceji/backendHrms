from rest_framework.response import Response
from rest_framework.decorators import api_view
from .db import db
import re
from datetime import date

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def today_str():
    return date.today().strftime("%Y-%m-%d")


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

    if db.employees.find_one({"email": data["email"]}):
        return Response({"error": "Email already exists"}, status=400)

    clean_data = {
        "employee_id": data["employee_id"],
        "full_name": data["full_name"],
        "email": data["email"],
        "department": data["department"],
    }

    db.employees.insert_one(clean_data)
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

    db.attendance.delete_many({"employee_id": emp_id})

    return Response({"message": "Employee deleted"})




@api_view(["POST"])
def mark_attendance(request):
    data = request.data

    required_fields = ["employee_id", "date", "status"]

    for field in required_fields:
        if not data.get(field):
            return Response({"error": f"{field} is required"}, status=400)

    employee = db.employees.find_one({"employee_id": data["employee_id"]})

    if not employee:
        return Response({"error": "Invalid employee ID"}, status=400)

    if data["status"] not in ["Present", "Absent"]:
        return Response({"error": "Status must be Present or Absent"}, status=400)

    if data["date"] > today_str():
        return Response({"error": "Cannot mark attendance for future date"}, status=400)

    existing = db.attendance.find_one({
        "employee_id": data["employee_id"],
        "date": data["date"]
    })

    if existing:
        return Response({
            "error": "Attendance already marked for this date"
        }, status=400)

    clean_data = {
        "employee_id": data["employee_id"],  
        "date": data["date"],
        "status": data["status"]
    }

    db.attendance.insert_one(clean_data)
    return Response({"message": "Attendance marked successfully"}, status=201)



@api_view(["GET"])
def get_attendance(request, emp_id):
    records = list(db.attendance.find(
        {"employee_id": emp_id},
        {"_id": 0}
    ))
    return Response(records)  
