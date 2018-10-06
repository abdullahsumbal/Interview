#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char * argv[]){
  char * string = malloc(100 * sizeof(char));
  scanf("%s", string);
  int len = strlen(string);
  for(int index = 0; index < len / 2; index++){
      if (string[index]  != string[len - 1 - index]){
        printf("Not Equal");
        return 0;
      }
  }
  printf("Equal");
}
