# To-Do List App

tasks=[] # An empty list to add tasks

def new_line():
    print("\n")

def add_task(tasks):
    tasks.append(input(f"Enter your task : "))

def view_all_tasks(tasks):
    print("S No.    TASKS")
    for i , task in enumerate(tasks,start=1):
        print(f"{i}   {task}")

def remove_all_tasks(tasks):
    print("Removing All Tasks...\n")
    j=1
    for i in tasks:
        print(f"Task {j} , {i} Removed")
        j=j+1
    tasks.clear()
    print("\nAll Tasks Removed")
        
def remove_specific_task(tasks):
    try:
        view_all_tasks(tasks)
        task_number=int(input("Enter the task number to remove it from the list : "))
        if task_number<1 or task_number>len(tasks):
            print("Enter Valid Task Number")
        else:
            tasks.pop(task_number-1)
            print("Task Removed")
    except ValueError:
        print("Enter an integer value.")

loop="running" # Loop is running

while loop=="running":
    print("Enter :\n0 To Exit\n1 To Add Task\n2 To View Tasks\n3 To Remove Task")
    
    try:
        choice=int(input("Enter your choice : "))
    except ValueError:
        print("Enter an integer value.")
        continue 

    if choice < 0 or choice > 3:
        print("Enter Valid Choice.\n")
    elif choice==0:
        print("Exiting The Program...")
        loop="stop"
        print("EXITED")
    elif choice==1:
        add_task(tasks)
        new_line()
    elif choice==2:
        new_line()
        if not tasks:
            print("NO TASKS TO SHOW PLEASE ADD TASKS FIRST")
        else:
            view_all_tasks(tasks)
            new_line()
    elif choice==3:
        if not tasks:
            print("NO TASKS TO REMOVE")
        else:
            choose=input("Enter (all) to remove all tasks or Enter (specific) to remove a specific task : ").lower()
            if choose=="all":
                remove_all_tasks(tasks)
                new_line()
            elif choose=="specific":
                remove_specific_task(tasks)
                new_line()
            else:
                print("Enter Valid Choice")