# -*- coding: windows-1251 -*-
import pandas as pd
from multiprocessing import Pool
from time import time
from matplotlib import pyplot as plt
import numpy as np


def min_finder(*data):
    '''
              Находит минимальное значение массива данных, игнорируя отсутствие данных
        '''
    first = list(data)
    minimal = 9999999999
    for i in first:
        if i < minimal and i != -1:
            minimal = i
    return minimal


df = pd.read_csv("data.csv", sep=",", encoding='windows-1251')

if __name__=="__main__":
    time_1 = time()
    lst=[]
    '''
                      Находим время выполнения программы при разном кол-ве процессов
                '''
    for i in range(1, 5):
        with Pool(i) as p:
            print(p.apply(min_finder, df["Активные случаи"].tolist()))
        a=time() - time_1
        lst.append(a)
        print(time() - time_1)
    print(lst)
    '''
                  Строим столбчатую диаграмму на основе времени
            '''
    fig = plt.figure(figsize=(10, 5))
    plt.ylabel('y')
    plt.xlabel('x')
    plt.title('y=sinc(x)')
    plt.bar(list(range(1,5)), lst, color='steelblue', width=0.5)
    plt.show()