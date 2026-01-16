# Todo List Application

A simple command-line todo list application built with Python.

## Description

This application allows users to manage their tasks through a simple CLI interface. Users can add tasks, mark them as complete, delete them, and view all tasks. All tasks are persisted to a JSON file.

## Language & Technologies

- **Language**: Python 3.9
- **Libraries**: 
  - `json` (standard library) - for file persistence
  - `os` (standard library) - for file operations

## Setup Instructions

1. Ensure Python 3.9 or higher is installed
2. No additional packages required (uses only standard library)

## How to Run

```bash
python todo.py
```

Or if you need to specify Python 3:

```bash
python3 todo.py
```

## Features Implemented

### Core Features
- ✅ Add new tasks
- ✅ Mark tasks as complete
- ✅ Delete tasks
- ✅ List all tasks with status
- ✅ Save tasks to file (persistence)

### Bonus Features
- ✅ Filter tasks by status (all/completed/pending)

## Usage Example

```
=== Todo List Application ===

1. Add task
2. Mark task as complete
3. Delete task
4. List all tasks
5. Filter tasks
6. Exit

Enter your choice: 1
Enter task description: Buy groceries
Task added successfully!

Enter your choice: 4
=== All Tasks ===
1. [PENDING] Buy groceries
2. [COMPLETED] Finish project

Enter your choice: 2
Enter task number to mark as complete: 1
Task marked as complete!
```

## File Structure

```
.
├── todo.py          # Main application file
├── tasks.json       # Data file (created automatically)
├── README.md        # This file
└── daily-goals.md   # Daily progress tracking
```

## Challenges Faced

1. **File Persistence**: Initially had issues with JSON encoding/decoding. Solved by using proper error handling and default values.

2. **User Input Validation**: Had to add validation to ensure users enter valid task numbers. Implemented try-except blocks and range checking.

3. **Task Numbering**: Keeping task numbers consistent when deleting tasks was tricky. Solved by renumbering tasks after each deletion.

## Future Improvements

If I had more time, I would add:
- Due dates and reminders
- Task priorities (high/medium/low)
- Task categories/tags
- Search functionality
- Task editing (update description)
- GUI version using tkinter or web interface
- Statistics (tasks completed today, this week, etc.)

## Testing

The application has been tested with:
- Adding multiple tasks
- Marking tasks as complete
- Deleting tasks
- File persistence (closing and reopening the app)
- Error cases (invalid input, missing file, etc.)

---

**Author**: Example Student  
**Week**: 01  
**Date**: [Date]
