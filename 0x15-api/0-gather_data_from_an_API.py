#!/usr/bin/python3
"""
Get's todo list for a given employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    id = sys.argv[1]
    employee = requests.get("{}/users/{}".format(url, id)).json()
    todos = requests.get("{}/todos".format(url), params={"userId": id}).json()

    completed = [task.get("title") for task in todos
                 if task.get("completed") is True]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee.get("name"), len(completed), len(todos)
        )
    )

    print("\n".join("\t {}".format(task) for task in completed))
