#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include  <stdlib.h>
#include <cs50.h>

int main(void)
{
    long long cardNumber;

    do
    {
        printf("Card Number: ");
        scanf("%lli",  &cardNumber);
        /*
        long long cardnumber = get_long_long("cardNumber: ");
    } 
    while (cardNumber < 0);

    //counts if no of digits == 13,15,or 16
    int count = 0; 
    long long digits = cardNumber; //digits in cardnumber
    while (digits > 0)
    {
        digits = digits/10;
        count++;
    }
    if ((count != 13) && (count != 15) && (count != 16))
    {
        printf("INVALID!\n");
    }
    
    //initialising number array with the cardnumbers reversed
    int number[count];
    for (int i=0; i < count; i++)
    {
        number[i] = cardNumber % 10; //reverses the cardnumber
        cardNumber = cardNumber / 10;
    }

    //doubling the cardnumbers, two steps from the second to the last digit
    int even_e;
    int total = 0;
    
    for (int i= 1; i < count; i+=2)
    {
        even_e = 2 * number[i]; //doubles and adds
        if (even_e > 9)
        {
            int firstDigit = even_e /  10;
            int lastDigit = even_e % 10;
            total = total + firstDigit + lastDigit;
        }
        else
        {
            total  = total + even_e;
        }
    }

    for (int j = 0; j < count; j+=2)
    {
        total = total + number[j];
    }
    
    //checking  validity of card
    if (count == 16)
    {
        if (total % 10 == 0 && number[15] == 3 && (number[14] == 4 || number[14] == 7))
        {
            printf("AMERICAN EXPRESS\n");
        }
        else if ((total % 10 == 0 && number[15] == 4))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }

    else if (count == 15)
    {
        if (total % 10 == 0 && number[14] == 5 && (number[13] == 1 || number[14] == 2 || number[14] == 3 || number[14] == 4 || number[14] == 5))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
        
    }
    
    else if (count == 13)
    {
        if (total  % 10 == 0 && number[12] == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }       
    }
    return 1;
}
