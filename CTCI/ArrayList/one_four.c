#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

char * int2bin(int i)
{
    size_t bits = sizeof(int) * CHAR_BIT;

    char * str = malloc(bits + 1);
    if(!str) return NULL;
    str[bits] = 0;

    // type punning because signed shift is implementation-defined
    unsigned u = *(unsigned *)&i;
    for(; bits--; u >>= 1)
        str[bits] = u & 1 ? '1' : '0';

    return str;
}

int main(int argc, char const *argv[]) {
  char * string = "anhjknna";
  int length = strlen(string);
  int checker = 0;
  for(int i = 0; i < length; i++){
    checker ^= (1 << (string[i] - 'a'));
  }
  printf("%s\n", int2bin(checker));
  if((checker & (checker - 1)) == 0){
    printf("It is True");
  }
  printf("It is False");
  return 0;
}
