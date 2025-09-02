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
        "status": "doing",
        "createdAt": formatted_now,
        "updatedAt": formatted_now
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_id})")


def list_tasks(status):
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No task at the moment")

    if len(status) == 0:
        print("Tasks: \n")
        for task in tasks:
            [print(f"{key}: {value}") for key, value in task.items()]
            print()
    elif status == "todo":
        print("Todo: \n")
        todo_tasks = [task for task in tasks if task["status"] == "todo"]
        for todo_task in todo_tasks:
            [print(f"{key}: {value}") for key, value in todo_task.items()]
            print()
    elif status == "done":
        print("Finished: \n")
        done_tasks = [task for task in tasks if task["status"] == "done"]
        for done_task in done_tasks:
            [print(f"{key}: {value}") for key, value in done_task.items()]
            print()
    elif status == "doing":
        print("In Progress: \n")
        in_progress_tasks = [
            task for task in tasks if task["status"] == "doing"]
        for in_progress_task in in_progress_tasks:
            [print(f"{key}: {value}")
             for key, value in in_progress_task.items()]
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
        status = sys.argv[2]
        if len(sys.argv) == 2:
            list_tasks(status="")
        elif status == "todo" or "done" or "doing":
            list_tasks(status)
        else:
            print("Usage: python task_cli list <optional: done, todo, doing>")
            sys.exit(1)

    else:
        print(f"Unknown command: {command}")
