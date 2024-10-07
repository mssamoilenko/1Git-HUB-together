FILENAME = ['tasks.txt']

# def load_task():
# 	pass

# def save_task():
# 	pass

tasks = ['help mom', 'clean windows', 'drink water']

def add_task(tasks: list, task: str): # list, str, ... - types of arguments for comfortable work
	tasks.append(task)

def edit_task(tasks: list, indexOfEditingTask: int, newTask: str):
	tasks[indexOfEditingTask] = newTask

def mark_ready_task(tasks: list, indexOfMarkingTask: int):
	tasks[indexOfMarkingTask] = f'"{tasks[indexOfMarkingTask]}" - DONE'

def delete_task():
	pass

# # test >>>

# print(tasks)

# add_task(tasks, input('new task: ')) 
# print(tasks)

# edit_task(tasks, int(input('index of task to edit: ')), input('new name of task: ')) # test
# print(tasks)

# mark_ready_task(tasks, int(input('index of task to mark as done: ')))
# print(tasks)

# # <<< test

def main():
	print('tasks:', tasks)
	print('''
	1. add new task
	2. edit existing task
	3. delete existing task
	4. mark existing task as done
		''')

	userInput = input('choose option: ')

	if userInput == '1':
		add_task(tasks, input('name of new task: '))
		print('successfully added new task.')
	elif userInput == '2':
		edit_task(tasks, int(input('index of task to edit: ')), input('new name for task: '))
		print('successfully edited task.')
	elif userInput == '3':
		delete_task()
	elif userInput == '4':
		mark_ready_task(tasks, int(input('index of task to mark as done: ')))
		print('successfully marked task as done.')

while True:
	main()