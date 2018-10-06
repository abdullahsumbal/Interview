#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv []) {

  //char * string = malloc(100 *sizeof(char));
  char string [100];
  char string1 [] = "dsjkfds";
  scanf("%s", string);
  printf("%d\n",strlen(string));

  for (int index =  strlen(string) - 1; index >= 0; index--){
    printf("%c", string[index]);
  }
  return 0;
}
