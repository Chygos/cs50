#include<stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>
#include <cs50.h>


int main(int argc, char* argv[] )// main accepts a command-line argument
{
    if (argc != 2) //prints if count of command-line  arg != 2
    {
        printf("Usage: ./sustitution key\n");
        return 1;
    }

    char* key = argv[1]; //initialising key array and passsing the value of arg[1] to it
    //checking key contains anything not letters
    for (int i = 0; i < strlen(key); i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Keys must contain letters only\n");
            return 1;
        }
    }

    //checking if there are repeated letters
    int keyCount = 0;
    for (int i= 0; key[i] != '\0'; i++)
    {
        for (int j=0; key[j] != '\0'; j++)
        {
            if (key[i] == key[j])
            {
                keyCount += 1;
            }
        }
    }

    //checking key length
    if (strlen(key) != 26)
    {
        printf("key must contain 26 characters\n");
        return 1;
    }

    else if (strlen(key) != 26 || keyCount - strlen(key) > 0)
    {
        printf("Key contains repeated letters\n");
        return 1;
    }


    //Get user input
    string text = get_string("plaintext: ");

     //creating arrays(strings)
    string plainText;
    string cipharText;

    plainText = text;
    cipharText = plainText;


    // //iteration
    for (int i = 0, n = strlen(plainText); i < n; i++)
    {
        if (isalpha(plainText[i]))
        {
            if (isupper(plainText[i]))
            {
                int pi = plainText[i] - 'A';
                int ci = key[pi];
                cipharText[i] = toupper(ci);
            }
            else if (islower(plainText[i]))
            {
                int pi = plainText[i] - 'a';
                int ci = key[pi];
                cipharText[i] = tolower(ci);
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