tasks = {}
def add_task(task_id, task_name):
    tasks[task_id] = {'Task': task_name, 'Status': 'Pending'}
    print(f'Task "{task_name}" added successfully!')

def update_task(task_id, task_name=None, status=None):
    if task_id in tasks:
        if task_name:
            tasks[task_id]['Task'] = task_name
        if status:
            tasks[task_id]['Status'] = status
        print(f'Task {task_id} updated successfully!')
    else:
        print(f'Task ID {task_id} not found.')

def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f'Task {task_id} deleted successfully!')
    else:
        print(f'Task ID {task_id} not found.')

def view_tasks():
    if tasks:
        print("\nTo-Do List:")
        for task_id, task_info in tasks.items():
            print(f"{task_id}: {task_info['Task']} - {task_info['Status']}")
    else:
        print("No tasks available.")

def main():
    while True:
        print("\nTo-Do List Options:")
        print("1. Add a new task")
        print("2. Update a task")
        print("3. Delete a task")
        print("4. View all tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_id = input("Enter Task ID: ")
            task_name = input("Enter Task Name: ")
            add_task(task_id, task_name)
        elif choice == '2':
            task_id = input("Enter Task ID: ")
            task_name = input("Enter new Task Name (leave blank if no change): ")
            status = input("Enter new Status (Pending/Completed, leave blank if no change): ")
            update_task(task_id, task_name if task_name else None, status if status else None)
        elif choice == '3':
            task_id = input("Enter Task ID to delete: ")
            delete_task(task_id)
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
