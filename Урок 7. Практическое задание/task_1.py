
from time import sleep
class TrafficLight:
    _states = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color
            print(f"Включен {self._color} сигнал на"
                  f" {sw_time} сек")

            sleep(sw_time)


traffic_light= TrafficLight()
traffic_light.running()
