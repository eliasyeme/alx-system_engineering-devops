#!/usr/bin/python3
"""
Get's todo list for a given users and exports to JSON.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(
            {
                user.get("id"): [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": user.get("username"),
                    }
                    for task in requests.get(
                        "{}/todos".format(url), params={"userId": user.get("id")}
                    ).json()
                ]
                for user in users
            },
            jsonfile,
        )
