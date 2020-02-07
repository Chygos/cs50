#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include  <stdlib.h>
#include <cs50.h>

int main(void)
{
    float money;
    int quarter = 25;
    int dime = 10;
    int fives = 5;
    int ones = 1;
    int result = 0;

    printf("Change: ");
    scanf("%f", &money);
    //or with cs50
    //cash = get_float("Change: ");

    //converting to kobo and removing thedecimal part
    int coins = 100 * money;
    while (coins >=  0)
    {
        if (coins >=  quarter)
        {
            coins -= quarter;
            result +=1;
        }
        else if (coins >= dime)
        {
            coins -= dime;
            result += 1;
        }
        else if (coins >= fives)
        {
            coins -= fives;
            result += 1;
        }
        else if (coins >= ones)
        {
            coins -= ones;
            result += 1;
        }
        else
        {
            break;
        }
    }
    printf("%d\n", result);
    return 0;
}
