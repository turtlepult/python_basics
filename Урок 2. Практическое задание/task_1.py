"""На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
"""
from random import randint

number_coins = randint(1, 20)
number_emblem_coins = randint(1, number_coins)
number_edge_coins = number_coins - number_emblem_coins

print(f"Минимальное количество монет которые нужно перевернуть: {number_edge_coins} "
      if number_edge_coins < number_emblem_coins else f"{number_emblem_coins}")
