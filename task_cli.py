import sys
import json
import os
import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
        return []

    with open(TASKS_FILE, 'r') as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)


def add_task(desc):
    tasks = load_tasks()

    if len(tasks) == 0:
        new_id = 1
    else:
        highest_id = max(task["id"] for task in tasks)
        new_id = highest_id + 1

    createdAt = datetime.datetime.now()
    formatted_now = createdAt.strftime("%B %d, %Y, %I:%M %p")

    new_task = {
        "id": new_id,
        "description": desc,
        "status": "todo",
        "createdAt": formatted_now,
        "updatedAt": formatted_now
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: ${new_id})")


def list_tasks(status):
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No task at the moment")

    print("Tasks: \n")
    for task in tasks:
        [print(f"{key}: {value}") for key, value in task.items()]
        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py add [args]")
            sys.exit(1)
        desc = sys.argv[2]
        add_task(desc)
    elif command == "list":
        if len(sys.argv) != 2:
            print("Usage: python task_cli.py list")
        list_tasks()
    elif command == ("list" & sys.argv[3]):
        status = sys.argv[3]
        list_tasks(status)

    else:
        print(f"Unknown command: {command}")
