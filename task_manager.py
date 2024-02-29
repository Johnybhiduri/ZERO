class ToDoApplication:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed' : False})

    def delete_task(self, index):
        del self.tasks[index]

    def mark_as_completed(self, index):
        if index >= len(self.tasks) or index < 0:
            print('task not added!')
        else:
            self.tasks[index]['completed'] = True

    def display_task(self):
        print('To-do-list:')
        for i, task in enumerate(self.tasks):
            status = 'completed' if task['completed'] else 'pending'
            print(f'{i+1}. Status : [{status}], Task :  {task["task"]}')

def main():

    to_do_list = ToDoApplication()

    while True:
        print('\n1. Add a task:')
        print('2. Delete a task:')
        print('3. Mark a task as completed:')
        print('4. Display the task:')
        print('5. Exit:')

        choice = int(input('\nEnter Your choice from 1 to 5...'))

        if choice == 1:
            task = input('\nEnter the task you want to add...')
            to_do_list.add_task(task)

        elif choice == 2:
            try:
                index = int(input('\nEnter the index of task you want to remove...')) - 1
                to_do_list.delete_task(index)
            except:
                print('Oops no task added to remmove! Add some task first...')

        elif choice == 3:
            try:
                index = int(input('\nEnter the index of the task you want to maek as complete...')) - 1
                to_do_list.mark_as_completed(index)
            except:
                print('Oops no such task to mark! Add the task first...')

        elif choice == 4:
            to_do_list.display_task()

        elif choice == 5:
            print('\nExiting...')
            break

        else:
            print('\nOops Invalid choice! Please try again!')

if __name__ == '__main__':
    main()
