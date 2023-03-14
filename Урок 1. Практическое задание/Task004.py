"""Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.
"""
revenue_value = int(input("enter the revenue value: "))
costs_value = int(input("enter the value of the company's costs: "))
if revenue_value>costs_value:
    print(f"Profit! Profitability = {((revenue_value-costs_value)/revenue_value)}")
else: print("Loss!")
number_employees_company = int(input("enter the number of employees of the company: "))
print(f"profit per employee = {(revenue_value-costs_value)/number_employees_company}")
