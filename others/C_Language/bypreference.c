
#include<stdio.h>

void B(int &worthRef) {
    worthRef += 1;
}

int main() {
    int netWorth = 55;
    B(netWorth);
    printf("%d", netWorth);
    return 0;
}
