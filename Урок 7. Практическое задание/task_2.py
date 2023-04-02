class Road():
    _length = int
    _width = int

    def calculation_asphalt(self, *args):
        _length = 5000
        _width = 20
        print(f"На дорогу потребуется {(_length * _width * args[0] * args[1]) / 1000} тонн")


calc = Road()
calc.calculation_asphalt(25, 0.05)
