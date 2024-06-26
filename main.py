import csv

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.completed else "Pending"
                print(f"{index}. {task.description} - {status}")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print("Task marked as completed...")
        else:
            print("Invalid task index.")

    def write_tasks(self, filename):
        tasks = [("Write report", "High"), ("Email client", "Medium")]  # Example data

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for task, priority in tasks:
                writer.writerow([task, priority])
    




def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Dump tasks into a file")
        print("5. exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            task_manager.add_task(description)
            print("Task added successfully.")
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: "))
            task_manager.mark_task_completed(task_index)
        elif choice == "4":
            file_name=input("Enter file into which data to be dumped: ")
            task_manager.write_tasks(file_name)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


