# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Enter number N= '))


i = 2 
list = []
num2 = num
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {num2} приведены в списке: {list}")