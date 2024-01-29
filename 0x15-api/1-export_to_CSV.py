#!/usr/bin/python3
"""
Get's todo list for a given employee ID and exports to CSV.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    id = sys.argv[1]
    employee = requests.get("{}/users/{}".format(url, id)).json()
    todos = requests.get("{}/todos".format(url), params={"userId": id}).json()

    with open("{}.csv".format(id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [
                    int(id),
                    employee.get("username"),
                    task.get("completed"),
                    task.get("title"),
                ]
            )
