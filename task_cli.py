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

    print(f"Task added successfully (ID: {new_id})")


def list_tasks(status=""):
    tasks = load_tasks()

    if not tasks:
        print("No tasks to list")
        return 

    status = status.lower()

    if status in ("", "all"):
        print("Tasks: \n")
        for task in tasks:
            [print(f"{key}: {value}") for key, value in task.items()]
            print()
    elif status in ("todo", "doing", "done"):
        filtered_tasks = [task for task in tasks if task["status"] == status]
        title = {
            "todo": "\nTodo: \n",
            "doing": "\nIn progress: \n",
            "done": "\nFinished: \n"
        }[status]
        print_tasks(filtered_tasks, title)
    else:
        print(f"Invalid status filter: {status}. Use 'todo', 'doing', 'done', or 'all'.")


def print_tasks(tasks, display_title):
    print(display_title)
    for task in tasks:
        [print(f"{key}: {value}") for key, value in task.items()]
        print()


def delete_task(task_id):
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No task to delete")
        sys.exit(1)

    task = find_task(tasks, task_id)
    if task == "not found":
        print("Task not found")
        sys.exit(1)

    tasks.remove(task)

    save_tasks(tasks)
    print(f"Task deleted (ID: {task_id})")


def update_task(task_id, description):
    tasks = load_tasks()
    task = find_task(tasks, task_id)

    if not tasks:
        print("No tasks to update")
        sys.exit(1)

    if task == "not found":
        print("Task not found")
        sys.exit(1)

    updatedAt = datetime.datetime.now().strftime("%B %d, %Y, %I:%M %p")

    task["description"] = description
    task["updatedAt"] = updatedAt

    save_tasks(tasks)
    print(f"Task updated (ID: {task_id})")


def mark_task(task_id, status):
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No task to mark")
        sys.exit(1)

    task = find_task(tasks, task_id)
    if task == "not found":
        print("Task not found")
        sys.exit(1)

    updatedAt = datetime.datetime.now().strftime("%B %d, %Y, %I:%M %p")

    task["updatedAt"] = updatedAt
    task["status"] = status

    save_tasks(tasks)
    print(f"Task {status} (ID: {task_id})")


def find_task(tasks, task_id):
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

        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python task_cli.py update <task id> <description>")
            sys.exit(1)
        task_id = int(sys.argv[2])
        description = " ".join(sys.argv[3:])
        update_task(task_id, description)
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py mark-in-progress <task id>")
            sys.exit(1)

        task_id = int(sys.argv[2])
        mark_task(task_id, "doing")
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py mark-done <task id>")
            sys.exit(1)

        task_id = int(sys.argv[2])
        mark_task(task_id, "done")

    else:
        print(f"Unknown command: {command}")
