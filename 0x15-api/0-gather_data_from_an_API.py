#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of an employee
using a REST API.
"""

import requests
import sys


def get_progress(employee_id):
    """
    Fetches and prints the TODO list progress of an employee.
    """
    base_api_url = "https://jsonplaceholder.typicode.com"
    user_api_url = f"{base_api_url}/users/{employee_id}"
    todos_api_url = f"{base_api_url}/todos?userId={employee_id}"

    user_response = requests.get(user_api_url)
    todos_response = requests.get(todos_api_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get("name")
    num_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    num_completed_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks("
        f"{num_completed_tasks}/{num_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo_list.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_progress(employee_id)
