#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Решить поставленную задачу: написать функцию,
вычисляющую среднее геометрическое
своих аргументов a1,a2, ... an
Если функции передается пустой список аргументов,
то она должна возвращать значение None
'''


def func(*arg):
    if arg:
        g = 1.0
        for i in arg:
            g *= i
        g = g ** (1 / len(arg))
        return g
    else:
        return None


if __name__ == '__main__':
    mass = list(map(float, input("Введите массив из чисел: ").split()))
    print(func(*mass))
