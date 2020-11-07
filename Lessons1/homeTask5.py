revenue = float(input("Введите значение выручки (тенге) - "))
costs = float(input("Введите значение издержек (тенге) - "))
result = revenue - costs
if result > 0:
    print(f"Поздравлем,Ваша компания работает с прибылью!")
elif result <0:
    print(f"Упс! Ваша компания в убытке!")
else:
    print(f"Прибыль ноль. Работаем дальше))")