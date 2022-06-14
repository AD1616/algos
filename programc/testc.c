#include <string.h>
#include <stdio.h>

int add(int num1, int num2);

int main() {
    printf("\t calculator \n --------------- \n");
    int addResult = add(5, 6);
    printf("%d",addResult);
    return 0;
}


int add(int num1, int num2) {
    return num1+num2;
}