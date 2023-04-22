class TypedMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=TypedMeta):
    pass


obj_1 = MyClass()
obj_2 = MyClass()

if id(obj_2) == id(obj_1):
    print("Переменные одной инстанции")
else:
    print("Ищи ошибки!")
