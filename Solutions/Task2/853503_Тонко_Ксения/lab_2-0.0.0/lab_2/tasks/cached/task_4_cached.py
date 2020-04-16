def cached(func):
    list_args = []
    list_result = []

    def wrapper(*args):
        func_list = [args, func.__name__]
        if func_list in list_args:
            index = list_args.index(func_list)
            result = list_result[index]
        else:
            result = func(*args)
            list_result.append(result)
            list_args.append(func_list)
        return result

    return wrapper
