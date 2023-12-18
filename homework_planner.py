#importing the module for file operations and serialization
import os 
import pickle 
#this intitialize the code with a filename so it can store the task
#this function also loads existing tasks from the file 
class HomeworkPlanner:
    def __init__(self, filename="homework_tasks.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()
#this code adds or store tasks in the empty list 
# it can check for an existing file
    def load_tasks(self):
        tasks = []
        if os.path.exists(self.filename):
            #reading the tasks from the file and converts them into a list of dictonaries 
            with open(self.filename, "r") as file:
                for line in file:
                    description, completed = line.strip().split(',')
                    tasks.append({"description": description, "completed": completed == "True"})
        return tasks
#this writes tasks to the file in a specific format 
    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task['description']},{task['completed']}\n")
#display in the terminal with the tasks 
    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task['description']} - {'Completed' if task['completed'] else 'Not Completed'}")
#add a new task with a description and the status in the planner 
    def add_task(self, description):
        task = {"description": description, "completed": False}
        self.tasks.append(task)
        self.save_tasks() #savs the planners task to the file 
        print(f"Task '{description}' added successfully.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            self.save_tasks()
            print(f"Task {task_index} marked as completed.")
        else:
            print("Invalid task index.")

#the problems i had with this code are trying to find out what was wrong with the code,
#i didnt know how to solve some of the errors in the code, such as trying to make the program make a new file,
#in a txt file format because it kept making a pkl file. at a certain point, i couldnt run the code in vs code 
#for some reason, but it was working at some point with functioning code. 