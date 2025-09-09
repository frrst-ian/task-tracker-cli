# Task Tracker CLI

A command-line task management tool built with Python for efficient task tracking and organization.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Roadmap.sh](https://img.shields.io/badge/Roadmap.sh-Project-orange.svg)](https://roadmap.sh/projects/task-tracker)

## Features

- Add, update, and delete tasks
- Mark tasks as in-progress or completed
- List tasks with status filtering
- Local JSON storage
- Comprehensive error handling

## Installation

```bash
git clone https://github.com/yourusername/task-tracker-cli.git
cd task-tracker-cli
```

Requires Python 3.x (no external dependencies).

## Usage

```bash
# Add tasks
python task_cli.py add "Buy groceries"

# Update tasks
python task_cli.py update 1 "Buy groceries and cook dinner"

# Mark status
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1

# List tasks
python task_cli.py list                # All tasks
python task_cli.py list todo          # Filter by status
python task_cli.py list not-done      # Incomplete tasks

# Delete tasks
python task_cli.py delete 1
```

## Task Structure

Tasks are stored in `tasks.json` with the following properties:
- `id`: Unique identifier
- `description`: Task description
