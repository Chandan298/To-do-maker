from cgitb import text
from pywebio.input import*
from pywebio.output import*
from functools import partial
taskongoing = False
# PEP8 Configurations.

def taskCompleted(btnName, task,tasks,b):
    if btnName == 'Complete' and b["status"] == True:
        if b['status'] == True:
            tasks.remove(task)
            clear('creatingTasks')
            print('Complete',b)
            put_table(
                [
                    [i, put_buttons(['Complete', 'Ongoing'],onclick = partial(taskCompleted, task = i,tasks = tasks,b =  test ))] for i in tasks
                ],scope = 'creatingTasks',
            )
            
        else:
            put_error(f'The Task of {task} has to be ongoing before it is completed', closable=True)
        return 0
    if btnName == 'Ongoing':
        ongoingmessage = put_info(f"The task {task} is currently ongoing", closable=True)
        b['status'] = True
        print('Ongoing',b)
        clear('creatingTasks')
           
        put_table(
            [
                [i, put_buttons(['Complete', 'Ongoing'],onclick = partial(taskCompleted, task = i,tasks = tasks,b =  test ))] for i in tasks
            ],scope = 'creatingTasks',
        )
        return 0
        
# {'name':task,'status':taskongoing}
        

alltasks = []
with use_scope('creatingTasks'):
    while True:
        task = input(label= "Enter Your Tasks", placeholder="WRITE HERE", required= True)
        test = {'name':task,'status':taskongoing}
        alltasks.append(task)
        clear('creatingTasks')
        print(test, task)
        put_table(
            [
                [i, put_buttons(['Complete','Ongoing'],onclick = partial(taskCompleted, task = i,tasks = alltasks, b = test ))] for i in alltasks
            ]
        )
        

# List Comprehension...
# for i in alltasks:
#   print(i)