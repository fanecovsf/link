def execute_tasks(*args):
    for action in args:
        try:
            action()
        except:
            break