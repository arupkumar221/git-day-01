import json
import os
from datetime import datetime

DATA_FILE = 'employees.json'


class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            'emp_id': self.emp_id,
            'name': self.name,
            'department': self.department,
            'salary': self.salary
        }


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                for emp in data:
                    employee = Employee(
                        emp['emp_id'],
                        emp['name'],
                        emp['department'],
                        emp['salary']
                    )
                    self.employees.append(employee)

    def save_data(self):
        with open(DATA_FILE, 'w') as file:
            json.dump([emp.to_dict() for emp in self.employees], file, indent=4)

    def add_employee(self):
        print('\n===== Add Employee =====')
        emp_id = input('Enter Employee ID: ')
        name = input('Enter Name: ')
        department = input('Enter Department: ')

        try:
            salary = float(input('Enter Salary: '))
        except ValueError:
            print('Invalid salary input!')
            return

        for emp in self.employees:
            if emp.emp_id == emp_id:
                print('Employee ID already exists!')
                return

        employee = Employee(emp_id, name, department, salary)
        self.employees.append(employee)
        self.save_data()
        print('Employee added successfully!')

    def display_employees(self):
        print('\n===== Employee List =====')

        if not self.employees:
            print('No employees found!')
            return

        print(f"{'ID':<10}{'Name':<20}{'Department':<20}{'Salary':<15}")
        print('-' * 65)

        for emp in self.employees:
            print(f"{emp.emp_id:<10}{emp.name:<20}{emp.department:<20}{emp.salary:<15}")

    def search_employee(self):
        print('\n===== Search Employee =====')
        search_id = input('Enter Employee ID: ')

        for emp in self.employees:
            if emp.emp_id == search_id:
                print('\nEmployee Found:')
                print(f'ID         : {emp.emp_id}')
                print(f'Name       : {emp.name}')
                print(f'Department : {emp.department}')
                print(f'Salary     : {emp.salary}')
                return

        print('Employee not found!')

    def update_employee(self):
        print('\n===== Update Employee =====')
        update_id = input('Enter Employee ID to update: ')

        for emp in self.employees:
            if emp.emp_id == update_id:
                print('Leave field empty to keep old value.')

                name = input(f'Enter new name ({emp.name}): ')
                department = input(f'Enter new department ({emp.department}): ')
                salary = input(f'Enter new salary ({emp.salary}): ')

                if name:
                    emp.name = name

                if department:
                    emp.department = department

                if salary:
                    try:
                        emp.salary = float(salary)
                    except ValueError:
                        print('Invalid salary! Keeping old salary.')

                self.save_data()
                print('Employee updated successfully!')
                return

        print('Employee not found!')

    def delete_employee(self):
        print('\n===== Delete Employee =====')
        delete_id = input('Enter Employee ID to delete: ')

        for emp in self.employees:
            if emp.emp_id == delete_id:
                self.employees.remove(emp)
                self.save_data()
                print('Employee deleted successfully!')
                return

        print('Employee not found!')

    def department_report(self):
        print('\n===== Department Report =====')

        if not self.employees:
            print('No employee data available!')
            return

        report = {}

        for emp in self.employees:
            dept = emp.department
            if dept not in report:
                report[dept] = {
                    'count': 0,
                    'total_salary': 0
                }

            report[dept]['count'] += 1
            report[dept]['total_salary'] += emp.salary

        print(f"{'Department':<20}{'Employees':<15}{'Total Salary':<20}{'Average Salary':<20}")
        print('-' * 75)

        for dept, data in report.items():
            avg_salary = data['total_salary'] / data['count']
            print(f"{dept:<20}{data['count']:<15}{data['total_salary']:<20.2f}{avg_salary:<20.2f}")

    def highest_salary(self):
        print('\n===== Highest Salary Employee =====')

        if not self.employees:
            print('No employee data available!')
            return

        highest = max(self.employees, key=lambda emp: emp.salary)

        print(f'Employee ID : {highest.emp_id}')
        print(f'Name        : {highest.name}')
        print(f'Department  : {highest.department}')
        print(f'Salary      : {highest.salary}')

    def export_report(self):
        print('\n===== Export Re
