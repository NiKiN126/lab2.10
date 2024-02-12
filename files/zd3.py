#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Есть списко студентов, в котором указано:
1. Имя студента
2. Общая сумма балов у студента
Найти студента с наивысшим баллом
'''


def func(**studs):
    count = 0
    for name, bal in studs.items():
        if bal > count:
            count = bal
    return f"Самый высокий балл у студента по имени: {name}"


if __name__ == '__main__':
    print(
        func(
            Олег=11,
            Сергей=12,
            Андрей=10,
            Илья=14
        )
   )
