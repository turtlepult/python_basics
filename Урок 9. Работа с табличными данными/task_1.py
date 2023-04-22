class OneOf():

    def __init__(self, *options):
        self.options = set(options)

    def __set__(self, obj, value):
        if value not in self.options:
            raise ValueError(
                f'"{value}" должно быть одним из {self.options}')


class IsNumber():

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'{value} не число')
        self.value = value

    def __get__(self, instance, cls):
        return self.value


class Radiobutton():
    current = OneOf('1-й вариант', '2-й вариант', '3-й вариант')

    def __init__(self, default) -> None:
        self.current = default


class Number():
    value = IsNumber()


num = Number()
num.value = 1
print(num.value)
num.value = '1'
print(num.value)
