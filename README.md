#Homework Planner

The Homework Planner is a command-line tool written in Python to help users manage and organize their homework tasks effectively. This program provides a simple interface for adding new tasks, marking them as completed, and viewing the current list of tasks.

#Features

- Display Tasks: View the list of current tasks along with their completion status.
- Add Task: Add a new task to the list with a provided description.
- Mark Task as Completed: Mark a task as completed based on its index.

#Usage

1. Clone the repository or download the `homework_planner.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `homework_planner.py`.
4. Run the script by executing `python homework_planner.py`.
5. Follow the on-screen menu to interact with the Homework Planner.

#File Storage

Tasks are stored in a text file named `homework_tasks.txt`. Each line in the file represents a task with the format: `description,completed`.
However, this part of the program may not work due to an error in the code...

#Example
 python homework_planner.py

Homework Planner Menu:
1. Display Tasks
2. Add Task
3. Mark Task as Completed
4. Exit

Enter your choice (1-4): 1
No tasks found.

Enter your choice (1-4): 2
Enter task description: Complete math assignment
Task 'Complete math assignment' added successfully.

Enter your choice (1-4): 1
Tasks:
1. Complete math assignment - Not Completed

Enter your choice (1-4): 3
Tasks:
1. Complete math assignment - Not Completed
Enter the task number to mark as completed: 1
Task 1 marked as completed.

Enter your choice (1-4): 1
Tasks:
1. Complete math assignment - Completed

Enter your choice (1-4): 4
Exiting Homework Planner. Goodbye!
