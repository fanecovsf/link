

def task(name:str, detail:bool=False):
    def decorator(action):
        def wrapper(*args, **kwargs):
            try:
                result =  action()
                print(f'Success on task: {name}')
                return result
            except Exception as e:
                print(f'''
Fail on task: {name}
                        ''')
                if detail:
                    print(f'''
--------------------
Detail: {str(e)}
                        ''')
                raise ValueError()

        return wrapper
    return decorator


def persistent_task(name:str, detail:bool=False):
    def decorator(action):
        def wrapper(*args, **kwargs):
            x = 0
            count = 0
            while x == 0:
                try:
                    result = action()
                    print(f'Success on task: {name}')
                    x += 1
                    return result     
                except Exception as e:
                    count += 1
                    print(f'''
Fail on task: {name}
--------------------
Failed {count} times
                        ''')
                    if detail:
                        print(f'''
--------------------
Detail: {str(e)}
                        ''')
        return wrapper
    return decorator
