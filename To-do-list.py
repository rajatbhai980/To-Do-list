def display_menu():#serially prints out the necessary items from menu
    print('Menu: ')
    print('1. Add Tasks')
    print('2. View Tasks')
    print('3. Mark As Done')
    print('4. Exit')

def add_tasks(tasks):
    task = input('Enter any task: ')#using tasks as a common parameter in all functions,task is appended in the tasks and stored in the tasks parameter which will act as a list
    tasks.append(task)
    print(' Task has been added! ')

def view_tasks(tasks):
    for i in tasks:#for the number of times there a the elements stored in tasks list this loop will print out the following
        print('tasks:\n')
        for i, task in enumerate(tasks):#and within this loop i will act as idex and task will act as the element inside the list due to enumerate function in python
            print(i+1,'.',task)
def mark_tasks_done(tasks):
    if not tasks: #not operator in python inverts the truth by converting true to false and false to true
        print('No task to mark as done. ')
        return

    view_tasks(tasks) #display's tasks with indices ,we are calling the task from the above function.
    index = int(input('Enter the task index to mark as done:')) - 1

    if 0 <= index < len(tasks): #to include all the index 0 and above and also within in the length of tasks
        removed_tasks = tasks.pop(index)# pop function in python is used to remove any element by specifying the index within the paranthesis
        print(f"The f'{removed_tasks} marked as done and been removed from the list. ")

    else:
        print('Invalid task index. ')
'''
def save_tasks(tasks):
    with open('tasks.txt' , 'w') as f:
        for task in tasks:#For the number of element in tasks list it will loop and serially write out that element in text file with spacing
            f.write(f'{task}'"\n")#\n is useful for latter on creating spaces using the splitlines. function

def load_tasks(tasks):
    try:
        with open('tasks.txt', 'r') as f:
            return f.read().splitlines()#read   is reading file function where as splitlines is the function for splitting every element divided by space as a individual element in list within the file
    except FileNotFoundError:
        return[]#returns empty list upon try mentioned eror
'''

#main program logic
def main():
    tasks = [] #load task from file

    while True:
        display_menu()#above written function that shows all the available function

        choice = input('Enter your choice: ')

        if choice == '1':
            add_tasks(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_tasks_done(tasks)
        elif choice == '4':
            print('Exiting....')
            save_tasks()#so the save task created above was for saving the file after we chose to exit . makes perfect sense:)
            break
        else:
            print('Invalid Choice!  Please Enter a valid option. ')

if __name__ == "__main__":#in-built function in python to know if running code is imported or not
  main()

    #what a wonderfully written code logic






