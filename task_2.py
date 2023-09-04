# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def dict_form(**kwargs) -> dict:
    return {value if value.__hash__ is not None else str(value): key for key, value in kwargs.items()}

print(dict_form(a=2, b=3, c='a'))
