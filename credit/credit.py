cardNumber = input("Card Number: ")

#checking user input
while True:
    if (cardNumber.isalpha()) or (cardNumber == '') or ("-" in cardNumber) or (int(cardNumber) < 0) :
        cardNumber = input("Card Number: ")
    else: break

#functions
def checkSumValidCard(cardNumber):
    """
    This checksums for digits in the card number and prints if the card is valid or not
    """
    total = 0
    cardNumber.reverse() #reverses the list
    
    #Visa= 13,16, American Express = 16, MasterCard = 15
    if len(cardNumber) not in [13,15,16]:
        print('INVALID')
#         print("Please input a valid  card")
    else:
        if len(cardNumber) in [13, 15, 16]:
            for _ , num_e in enumerate(cardNumber[1::2],1): #takes from the second to the last digit
                even = 2 * int(num_e)
                if even > 9:
                    lastDigit = even % 10
                    firstDigit = even // 10
                    total = total + lastDigit + firstDigit
                else:
                    total = total + even
            for _, num_o in enumerate(cardNumber[::2], 1):
                total = total + int(num_o)
        
        #checking valid card
        cardNumber.reverse() #reversing back to original
        if total % 10 == 0 and int(str(cardNumber[0]) + str(cardNumber[1])) in [34, 37]: print("AMERICAN EXPRESS")
        elif total % 10 == 0 and  int(str(cardNumber[0]) + str(cardNumber[1])) in [51,52,53,54,55]: print("MASTERCARD")
        elif total % 10 == 0 and int(str(cardNumber[0])) == 4: print("VISA")
        else: print("INVALID")


if __name__ == "__main__":
    cardNumber = [int(x) for x in cardNumber]
    checkSumValidCard(cardNumber)
