#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <locale.h>


int past(int h, int m, int s){
    int soma = (h*60*60*1000)+(m*60*1000)+(s*1000);
    return (soma);
}


int main (){
    setlocale(LC_ALL, "portuguese");

    printf("Insira os valores em horas, minutos e segundos: \n");
    int h = 0;
    scanf("%d", &h);
    int m = 0;
    scanf("%d", &m);
    int s = 0;
    scanf("%d", &s);
    printf("Tempo em milisegundos após a meia noite: %d",  past(h,m,s));

	return 0;
}
