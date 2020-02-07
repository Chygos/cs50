#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
int main(void)
{
    string text = get_string("Enter Text: ");

    int words = 0;
    int letters = 0;
    int sentence = 0;

    for (int i=0; i < strlen(text); i++)
    {
        if (text[i] == '!' || text[i] == '.' || text[i] == '?')
        {
            sentence+=1;
        }

    }
    // printf("%i",sentence);
    // printf("\n");

    for (int i= 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters += 1;
        }
    }
    // printf("%i", letters);
    // printf("\n");

    for (int i = 0; i <= strlen(text); i++)
    {
        if (isspace(text[i]) || text[i] == '\0' || text[i] == ' ')
        {
            words += 1;
        }
    }
    // printf("%i", words);
    // printf("\n");

    float L = ((float) letters/words) * 100;
    float S = ((float) sentence/words) * 100;
    float Coleman_Liau_index = 0.0588 * L - 0.296 * S - 15.8;

    if (Coleman_Liau_index >= 16)
    {
        printf("Grade 16+");
    }
    else if (Coleman_Liau_index < 1)
    {
        printf("Before Grade 1");
    }
    else if (Coleman_Liau_index >= 1 || Coleman_Liau_index < 17)
    {
        printf("Grade %i", (int) round(Coleman_Liau_index));
    }
    printf("\n");
    // printf("%d\n%d\n%d\n", words,letters,sentence);

}