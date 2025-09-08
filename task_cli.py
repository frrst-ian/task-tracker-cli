import sys
import json
import os
import datetime

TASKS_FILE = "tasks.json"

# --------------------- File Handling ---------------------


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
        return []

    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# --------------------- Core Commands ---------------------


def add_task(desc):
    tasks = load_tasks()
    new_id = max([task["id"] for task in tasks], default=0) + 1
    now = datetime.datetime.now().strftime("%B %d, %Y, %I:%M %p")

    new_task = {
        "id": new_id,
        "description": desc,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")


def list_tasks(status=""):
    tasks = load_tasks()
    status = status.lower()

    if not tasks:
        print("No tasks to list.")
        return

    # Handle filters
    if status in ("", "all"):
        filtered_tasks = tasks
        title = "All Tasks:\n"
    elif status == "todo":
        filtered_tasks = [t for t in tasks if t["status"] == "todo"]
        title = "Todo Tasks:\n"
    elif status == "in-progress":
        filtered_tasks = [t for t in tasks if t["status"] == "in-progress"]
        title = "In-progress Tasks:\n"
    elif status == "done":
        filtered_tasks = [t for t in tasks if t["status"] == "done"]
        title = "Finished Tasks:\n"
    elif status == "not-done":
        filtered_tasks = [t for t in tasks if t["status"] in ("todo", "in-progress")]
        title = "Not Done Tasks:\n"
    else:
        print(
            f"Invalid status filter: {status}. Use 'todo', 'in-progress', 'done', 'not-done', or 'all'.")
        return

    if not filtered_tasks:
        print(f"No tasks found for filter '{status}'.")
        return

    print_tasks(filtered_tasks, title)


def print_tasks(tasks, display_title):
    print(display_title)
    for task in tasks:
        [print(f"{k}: {v}") for k, v in task.items()]
        print()


def delete_task(task_id):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if task == "not found":
        print("Task not found.")
        return
    tasks.remove(task)
    save_tasks(tasks)
    print(f"Task deleted (ID: {task_id})")


def update_task(task_id, description):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if task == "not found":
        print("Task not found.")
        return
    task["description"] = description
    task["updatedAt"] = datetime.datetime.now().strftime("%B %d, %Y, %I:%M %p")
    save_tasks(tasks)
    print(f"Task updated (ID: {task_id})")


def mark_task(task_id, status):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if task == "not found":
        print("Task not found.")
        return
    task["status"] = status
    task["updatedAt"] = datetime.datetime.now().strftime("%B %d, %Y, %I:%M %p")
    save_tasks(tasks)
    print(f"Task marked as {status} (ID: {task_id})")


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return "not found"


# --------------------- CLI Parsing ---------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [args]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py add <task description>")
            sys.exit(1)
        desc = " ".join(sys.argv[2:])
        add_task(desc)

    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else ""
        list_tasks(status)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py delete <task id>")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            sys.exit(1)
        delete_task(task_id)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python task_cli.py update <task id> <description>")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            sys.exit(1)
        description = " ".join(sys.argv[3:])
        update_task(task_id, description)

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py mark-in-progress <task id>")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            sys.exit(1)
        mark_task(task_id, "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py mark-done <task id>")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            sys.exit(1)
        mark_task(task_id, "done")

    else:
        print(f"Unknown command: {command}")
