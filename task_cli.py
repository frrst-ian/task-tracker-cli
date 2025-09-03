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
        print("No task to lsit")

    if len(status) == 0 or status == "all":
        print("Tasks: \n")
        for task in tasks:
            [print(f"{key}: {value}") for key, value in task.items()]
            print()
    elif status == "todo":
        task = [task for task in tasks if task["status"] == "todo"]
        print_tasks(task, "\nTodo: \n")
    elif status == "done":
        task = [task for task in tasks if task["status"] == "done"]
        print_tasks(task, "\nFinished: \n")
    elif status == "doing":
        in_progress_tasks = [
            task for task in tasks if task["status"] == "doing"]
        print_tasks(in_progress_tasks, "\nIn progress: \n")

    else:
        print("Invalid Status")
        sys.exit(1)


def print_tasks(tasks, display_title):
    print(display_title)
    for task in tasks:
        [print(f"{key}: {value}") for key, value in task.items()]
        print()


def delete_task(task_id):
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No task delete")

    task = find_tasks(tasks, task_id)
    if task == "not found":
        print("Task not found")
        sys.exit(1)

    tasks.remove(task)

    save_tasks(tasks)
    print(f"Task deleted (ID: {task_id})")


def find_tasks(tasks, task_id):
    for task in tasks:
        if (task["id"] == task_id):
            return task
    return "not found"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py add <task description>")
            sys.exit(1)
        desc = sys.argv[2]
        add_task(desc)
    elif command == "list":
        if len(sys.argv) < 3:
            list_tasks("")
        else:
            status = sys.argv[2]
            if status == "todo" or status == "done" or status == "doing":
                list_tasks(status)
            else:
                print("Usage: python task_cli list <optional: done, todo, doing>")
                sys.exit(1)
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py delete <task id>")
            sys.exit(1)
        task_id = sys.argv[2]
        task_int_id = int(task_id)
        delete_task(task_int_id)

    else:
        print(f"Unknown command: {command}")
