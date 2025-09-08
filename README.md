# Task Tracker CLI 📝

# Overview

The Task Tracker CLI is a simple command-line tool to manage your tasks efficiently. It allows you to add, update, delete, mark, and list tasks with ease, storing all data in a local JSON file. Perfect for practicing filesystem operations, CLI design, and Python scripting.

# Features

Add tasks with a description.

Update task descriptions.

Delete tasks by ID.

Mark tasks as in-progress or done.

List tasks: all, by status (todo, in-progress, done), or incomplete (not-done).

Tasks include metadata: id, description, status, createdAt, updatedAt.

# Usage

Run the CLI from the terminal:

## Adding a task
python task_cli.py add "Buy groceries"  

## Updating a task
python task_cli.py update 1 "Buy groceries and cook dinner"  

## Deleting a task
python task_cli.py delete 1  

## Marking a task
python task_cli.py mark-in-progress 1  
python task_cli.py mark-done 1  

## Listing tasks
python task_cli.py list
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
python task_cli.py list not-done

# Task Structure

Each task is stored in tasks.json and has the following properties:

- id: Unique identifier

- description: Task description

- status: todo, in-progress, or done

- createdAt: Timestamp of creation

- updatedAt: Timestamp of last update

- Requirements

Python 3.x

No external libraries required

Runs entirely in the terminal

## Notes

Tasks are saved in tasks.json in the current directory.

Invalid inputs are handled gracefully with informative messages ⚠️.

Designed for simplicity and productivity.