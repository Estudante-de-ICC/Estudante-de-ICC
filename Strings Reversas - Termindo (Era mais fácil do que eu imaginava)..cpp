#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
using namespace std ;


string ReversedString (string str)
{
    int i = 0;

    while (str[i] != '\0')
    {
        i++;
    }

    char p[i];

    for (int k = 0; k < i; k++)
        {
            p[k] = str[i-k-1];

        }


    return p;
}


int main()
{
    string x = "CodeWars Is The Best";


    std::cout<< ReversedString(x)<< endl;



    return 0;
};
