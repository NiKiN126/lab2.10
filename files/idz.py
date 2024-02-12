#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Сумму аргументов, расположенных после последнего аргумента, равного нулю.
'''


def func(*mass):
    summ = 0
    if mass:
        for i, x in enumerate(mass):
            if x < 0:
                count: object
                for count in mass[i+1:]:
                    if count < 0:
                        break
                    else:
                        summ += count
                return summ
    else:
        return None


if __name__ == '__main__':
    mass = list(map(float, input("Введите массив из чисел: ").split()))
    print(func(*mass))
