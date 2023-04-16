from _datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        call_time = datetime.now().strftime('%d-%m-%Y Время %H:%M:%S')
        old_function_name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'Время вызова: {call_time}, '
                       f'Название: - {old_function_name}, '
                       f'Аргументы: - {args, kwargs}, '
                       f'Значение: - {result}')
        return result

    return new_function


def logger_func(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            call_time = datetime.now().strftime('%d-%m-%Y Время %H:%M:%S')
            old_function_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'Время вызова: {call_time}, '
                           f'Название: - {old_function_name}, '
                           f'Аргументы: - {args, kwargs}, '
                           f'Значение: - {result}')
            return result

        return new_function

    return __logger
