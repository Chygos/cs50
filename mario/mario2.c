#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 0 || n > 8);

    //prints left and right aligned bricks
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j < n-i; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        for (int l = 0; l <= n; l++)
        {
            printf(" ");
        }
        for (int m = 0; m < i; m++)
        {
            printf("#");
        }
        printf("\n");
    }
}
