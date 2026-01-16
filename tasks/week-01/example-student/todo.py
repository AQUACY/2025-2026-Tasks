"""
Todo List Application
A simple CLI todo list manager with file persistence.
"""

import json
import os
from datetime import datetime


class Task:
    """Represents a single task."""
    
    def __init__(self, description, status="pending"):
        self.description = description
        self.status = status
        self.created_at = datetime.now().isoformat()
    
    def mark_complete(self):
        """Mark the task as completed."""
        self.status = "completed"
    
    def __str__(self):
        status_icon = "✅" if self.status == "completed" else "⬜"
        return f"{status_icon} {self.description}"


class TodoList:
    """Manages a collection of tasks."""
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, description):
        """Add a new task to the list."""
        if description.strip():
            task = Task(description)
            self.tasks.append(task)
            self.save_tasks()
            return True
        return False
    
    def mark_task_complete(self, task_number):
        """Mark a task as complete by its number."""
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_complete()
            self.save_tasks()
            return True
        return False
    
    def delete_task(self, task_number):
        """Delete a task by its number."""
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            self.save_tasks()
            return True
        return False
    
    def list_tasks(self, filter_status=None):
        """List all tasks, optionally filtered by status."""
        filtered_tasks = self.tasks
        
        if filter_status == "completed":
            filtered_tasks = [t for t in self.tasks if t.status == "completed"]
        elif filter_status == "pending":
            filtered_tasks = [t for t in self.tasks if t.status == "pending"]
        
        return filtered_tasks
    
    def save_tasks(self):
        """Save tasks to a JSON file."""
        try:
            tasks_data = [
                {
                    "description": task.description,
                    "status": task.status,
                    "created_at": task.created_at
                }
                for task in self.tasks
            ]
            with open(self.filename, 'w') as f:
                json.dump(tasks_data, f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    tasks_data = json.load(f)
                    self.tasks = [
                        Task(task['description'], task['status'])
                        for task in tasks_data
                    ]
            except Exception as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []


def display_tasks(todo_list, filter_status=None):
    """Display tasks in a formatted way."""
    tasks = todo_list.list_tasks(filter_status)
    
    if not tasks:
        status_text = filter_status if filter_status else "all"
        print(f"\nNo {status_text} tasks found.")
        return
    
    print(f"\n=== {'All Tasks' if not filter_status else filter_status.capitalize() + ' Tasks'} ===")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def get_user_choice():
    """Get and validate user menu choice."""
    try:
        choice = int(input("\nEnter your choice: "))
        return choice
    except ValueError:
        return None


def main():
    """Main application loop."""
    todo_list = TodoList()
    
    print("=== Todo List Application ===\n")
    
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Mark task as complete")
        print("3. Delete task")
        print("4. List all tasks")
        print("5. Filter tasks")
        print("6. Exit")
        
        choice = get_user_choice()
        
        if choice == 1:
            description = input("Enter task description: ")
            if todo_list.add_task(description):
                print("Task added successfully!")
            else:
                print("Error: Task description cannot be empty.")
        
        elif choice == 2:
            display_tasks(todo_list)
            try:
                task_num = int(input("\nEnter task number to mark as complete: "))
                if todo_list.mark_task_complete(task_num):
                    print("Task marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == 3:
            display_tasks(todo_list)
            try:
                task_num = int(input("\nEnter task number to delete: "))
                if todo_list.delete_task(task_num):
                    print("Task deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == 4:
            display_tasks(todo_list)
        
        elif choice == 5:
            print("\nFilter by:")
            print("1. All tasks")
            print("2. Completed tasks")
            print("3. Pending tasks")
            filter_choice = get_user_choice()
            if filter_choice == 1:
                display_tasks(todo_list)
            elif filter_choice == 2:
                display_tasks(todo_list, "completed")
            elif filter_choice == 3:
                display_tasks(todo_list, "pending")
            else:
                print("Invalid choice.")
        
        elif choice == 6:
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
