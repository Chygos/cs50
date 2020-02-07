#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

/*
Caesar.c
Program that encrypts messages using Caesar's cipher.
This program accepts a command-line argument of a non-negative integer and raises an error if it is not included
*/
int main(int argc,  char* argv[])
{
    //argc = argument count
    //argv = argument vector
    //atoi = converts numeric strings to digits

    if (argc != 2)
    {
        printf("Usage: ./caesar key");
        return 1;
    }
    else if (!isdigit(*argv[1]))
    {
        printf("Usage: ./caesar key");
        return 1;
    }

    int key = atoi(argv[1]);
    if (key < 0)
    {
        printf("Non-negative integers only");
        return 1;
    }


    //Get user input
    string text = get_string("plaintext: ");

    //creating arrays(strings)
    string plainText;
    string cipharText;

    plainText = text;
    cipharText = plainText;


    for(int i = 0, n= strlen(plainText); i < n; i++)
    {
        if (isalpha(plainText[i]))
        {
            if (isupper(plainText[i]))
            {
                int pi = plainText[i] - 'A'; //65 => ascii value for "A"
                int ci = (pi + key) % 26;

                cipharText[i] = ci + 'A';
            }
            else if (islower(plainText[i]))
            {
                int pi = plainText[i] - 'a'; //97 =>ascii value for "a"
                int ci = (pi + key) % 26;

                cipharText[i] = ci + 'a';
            }
        }
        else
        {
            cipharText[i] = plainText[i];
        }
    }
    printf("ciphertext: %s\n", cipharText);
    return 0;
}