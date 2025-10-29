#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    m = int(input("Введите цифру от 1 до 4: "))

    if m == 1:
        print("Декабрь, январь, февраль")
    elif m == 2:
        print("Март, апрель, май")
    elif m == 3:
        print("Июнь, июль, август")
    elif m == 4:
        print("Сентябрь, октябрь, ноябрь")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)