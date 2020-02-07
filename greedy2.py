from collections import Counter
import time

def greedy2(money,coins):
    result = 0
    
    #checking if input is a string or value is negative
    while True:
        if (money.isalpha() or float(money) < 0):
            money= input("Change: ")
        else: break
    
    money = float(money) #accepts floating numbers
    cents =  int(100*money) #converting to integer

    while cents >= 0:
        if cents >= coins[0]:
            cents -= coins[0]
            money_list.append(coins[0])
            result += 1

        elif cents >= coins[1]:
            cents -= coins[1]
            money_list.append(coins[1])
            result += 1
        
        elif cents >= coins[2]:
            cents -= coins[2]
            money_list.append(coins[2])
            result += 1
        
        elif cents >= coins[3]:
            cents -= coins[3]
            money_list.append(coins[3])
            result += 1
        else: break
    return result
        
coins = [25,10, 5, 1]
money_list = []
money= input("Change: ")
t1= time.time()
result= greedy2(money,coins)
t2 = time.time()

print(result)
print(Counter(money_list))

print(t2-t1)