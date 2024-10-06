""" Some useful callback """

run_function = lambda *args, **kwargs: lambda func: func(*args, **kwargs)
""" When you have a function list and only want to call them, don't important the return, use this """

def setter(obj, field):
    def inner(param):
        if param != None:
            setattr(obj, field, param)
    return inner

def intDict(key, value):
    v = value if value != None else 0
    return int(v)