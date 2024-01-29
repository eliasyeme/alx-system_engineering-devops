#!/usr/bin/python3
"""
Get's todo list for a given employee ID and exports to JSON.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    id = sys.argv[1]
    employee = requests.get("{}/users/{}".format(url, id)).json()
    todos = requests.get("{}/todos".format(url), params={"userId": id}).json()

    with open("{}.json".format(id), "w") as jsonfile:
        json.dump(
            {
                id: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": employee.get("username"),
                    }
                    for task in todos
                ]
            },
            jsonfile,
        )
