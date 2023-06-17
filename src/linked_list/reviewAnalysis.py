from circularDoublyLinkedList_copy import *

def load_data(dataset:CircularDoublyLinkedList):
    with open('amazon_reviews_us_Video_Games_v1_00.tsv', 'r', encoding='UTF-8') as file:
        cnt = 0
        keys = []

        for line in file:
            temp = {}
            fileds = line.split('\t')

            if cnt == 0:
                keys = fileds; keys[-1] = keys[-1].replace('\n', '')
                cnt+=1
                continue
            if cnt > 10000: break #데이터 수량 정하기

            for filed, key in zip(fileds, keys):
                temp[key] = filed.replace('\n',''); 

            dataset.append(temp)
            cnt+=1

def get_data(dataset:CircularDoublyLinkedList):
    filtered = dataset.filter(CircularDoublyLinkedListFilter())

    ratelist = [['별점 1점'],['별점 2점'],['별점 3점'],['별점 4점'],['별점 5점']]
    tmp = 0

    for rated, element in zip(filtered, ratelist):
        for product in rated:
            element.append(product['product_title'])
        element = list(set(element)) #중복제거
        element.sort(reverse=True)
        print(element, '\n')
        tmp += len(element)
    print(tmp)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_rate(dataset:CircularDoublyLinkedList, product_title):
    filtered = dataset.filter(CircularDoublyLinkedListFilter(), product_title)
    # print(filtered)
    frequency = []
    
    for i in range(5):
        frequency.append(filtered.count(i+1))
    
    # plt.hist(filtered, label=product_title + " star rate",histtype='bar', bins = 5)
    plt.bar([1,2,3,4,5], frequency, width=0.7)
    plt.title(product_title + " star rate distribution")
    plt.xlabel('star rate')
    plt.ylabel('number of reviews')
    plt.legend()
    plt.savefig("rate.png")
    plt.show()


dataset = CircularDoublyLinkedList()
load_data(dataset)
get_data(dataset)
get_rate(dataset, "Grand Theft Auto V")