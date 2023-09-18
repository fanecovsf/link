
def execute_tasks(*args):
    for action in args:
        try:
            action(*args)
        except:
            break

    print('Execution terminated.')