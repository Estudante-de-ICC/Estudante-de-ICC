#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
using namespace std;

std::string DNAtoRNA(std::string dna)
{
    int i = 0;
    while (dna[i] != '\0')
        {
            i++;

        }
    char p[i];

    for (int k = 0; k < i; k++)
        {
            if (dna[k] == 'T')
                dna[k] = 'U';

        }



  return dna;
}

int main ()
{
    string x = "GCAT";
    std::cout<<DNAtoRNA(x)<<endl;


	return 0;
}
