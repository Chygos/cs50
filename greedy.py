from collections import Counter
import time


def greedy(money):
    #checking if input is a string or value is negative
    
    while (money.isalpha() or float(money) < 0):
        money = input("Change: ")
    else:
        money = float(money) #accepts floating numbers
        cents =  int(100*money) #converting to integer

        """
        Divide cents by 25; followed by its remainder after dividing by 10; then by dividing the remainder of 
        what is left after dividing 25 and 10 by 5 and then finally get the remainder after dividing the cents by
        25,10 and 5; then add all up        
        """
        result = (cents // 25) + ((cents % 25) // 10) + ((cents % 25 % 10) // 5) +  (cents % 25 % 10 % 5)
    return result



money = input("Change: ")
coins = [25,10,5,1]
coins_list = [] #stores the list of coins


t1 = time.time()
result = greedy(money)
t2 = time.time()
print("Total Coins: %s" %result)
print(t2-t1)


