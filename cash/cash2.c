#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    int quarter = 25;
    int dime = 10;
    int fives = 5;
    int ones = 1;

    float coins;
    do
    {
        coins = get_float ("Change owed: ");
    }
    while (coins < 0);

    coins = round(100 * coins);
    int result = 0;

    while (coins >= 1)
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
