#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {

  int arr[] = { 2, 5, 7, 1, 9, 3, 9 };
  int n = sizeof(arr) / sizeof(arr[0]);
  int m = 4;
  printf("%f",average(arr, n, m));
  return 0;
}

int average(int array [] , int length, int window){

  if(window > length){
    return 0;
  }

  float total = 0;
  float current = 0;

  for (int i = 0; i < window; i++){
    total += array[i];
  }

  current = total / window;

  for(int i = window; i < length; i++){
    total += array[i];
    total -= array[i-window];
    current+=total/window;
  }

printf("%f",current/(length-window+1));

  return current/(length-window+1);

}
