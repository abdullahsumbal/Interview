#include <stdio.h>
#include <stdlib.h>

int main(int argc ,char * argv[]){
  int base = atoi(argv[1]);
  int height =  atoi(argv[2]);

  printf("Base :%d\n", base);
  printf("height :%d\n", height);

  printf("\n");
  float incr = 0;
  for (int row = 0; row < height; row ++){
    incr += (float)base / (float)height;
    for(int column = 0; column < ((int)incr < 1 ? 1: (int)incr)   ; column++){
      printf("*");
    }
    printf("\n");
  }

  // int base = atoi(argv[1]);
  // int height =  atoi(argv[2]);
  //
  // printf("Base :%d\n", base);
  // printf("height :%d\n", height);
  //
  // printf("\n");
  // for (int row = 1; row <= height; row ++){
  //   for(int column = 1; column <= row; column++){
  //     printf("*");
  //   }
  //   printf("\n");
  // }
}
