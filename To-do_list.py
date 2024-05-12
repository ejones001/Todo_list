class Task:
    def __init__(self, title="Incomplete"):
        self.title = title
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                status = "Complete" if task.completed else "Incomplete"
                print(f"{i}. {task.title} - {status}")

    def mark_task_as_complete(self, index):
        try:
            index = int(index)
            if 1 <= index <= len(self.tasks):
                self.tasks[index - 1].mark_as_completed()
                print("Task marked as complete.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a valid task index.")

    def delete_task(self, index):
        try:
            index = int(index)
            if 1 <= index <= len(self.tasks):
                del self.tasks[index - 1]
                print("Task deleted.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a valid task index.")

def main():
    todo_list = ToDoList()
    print("Welcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter the title of the task: ")
            todo_list.add_task(title)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            index = input("Enter the index of the task to mark as complete: ")
            todo_list.mark_task_as_complete(index)
        elif choice == "4":
            index = input("Enter the index of the task to delete: ")
            todo_list.delete_task(index)
        elif choice == "5":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
