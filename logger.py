from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            with open(path, "a", encoding='utf-8') as file:
                log = f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} " \
                      f"call {old_function.__name__}" \
                      f"({', '.join([str(arg) for arg in args])}" \
                      f"{', ' if len(args) and len(kwargs) else ''}" \
                      f"{', '.join([key + '=' + str(value) for key, value in kwargs.items()])}); "
                file.write(log)

            result = old_function(*args, **kwargs)

            with open(path, "a", encoding='utf-8') as file:
                log = f"result: {result}\n"
                file.write(log)

            return result

        return new_function

    return __logger
