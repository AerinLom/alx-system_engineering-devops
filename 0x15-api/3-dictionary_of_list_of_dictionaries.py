#!/usr/bin/python3
"""
This script fetches and exports the TODO list of all employees with a REST API.
"""
import json
import requests


def get_user_progress():
    """
    Fetches and exports the TODO list of all employees to a JSON file.
    """
    base_api_url = "https://jsonplaceholder.typicode.com"
    user_api_url = f"{base_api_url}/users"

    all_users = requests.get(user_api_url).json()

    dict_of_tasks = {}
    for user in all_users:
        user_id = user['id']
        username = user['username']
        todo_api_url = f"{base_api_url}/users/{user_id}/todos"
        tasks = requests.get(todo_api_url).json()
        dict_of_tasks[user_id] = [
            {
                'username': username,
                'task': task['title'],
                'completed': task['completed']
            }
            for task in tasks
        ]

    with open("todo_all_employees.json", mode='w') as jsonfile:
        json.dump(dict_of_tasks, jsonfile)


if __name__ == "__main__":
    get_user_progress()
