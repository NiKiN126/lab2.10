#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Решить поставленную задачу: написать функцию,
вычисляющую среднее гармоническое
своих аргументов a1,a2, ... an
Если функции передается пустой список аргументов,
то она должна возвращать значение None
'''


def func(*arg):
    summ = 0
    if arg:
        for i in arg:
            if i == 0:
                return None
            else:
                summ += 1 / float(i)
        otvet = 1 / (1 / len(arg) * summ)
        return otvet
    else:
        return None


if __name__ == '__main__':
    mass = list(map(float, input("Введите массив из чисел: ").split()))
    print(func(*mass))
