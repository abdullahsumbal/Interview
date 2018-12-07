#include <stdio.h>

// To execute C, please define "int main()"

// int *A = ( 3,  5,  4,  6,  2,  5,  5,  7,  6,  8)
//
//      A = ( 3,  5,  4,  6,  2,  7,  8,  X,  X,  X)
// return 7

void swapback(int * A, int index, int size){

 while(index < size - 1){


   A[index] = A[index+1];
    index++;

 }

}

int countUnique (int * A, int size){

 int dup = 0;
  for (int i = 0; i < size - 1; i++){
    for(int j = i+1; j < size - dup; j++){
      //printf("%d\n", *(A + j));
      if(A[i] == A[j]){
        // iter until see not 5
        // swap back
        swapback(A, j, size);
        dup++;
        j--;
        //3,  5,  4,  6,  2,  5,  7,  6,  8, X , X
      }
    }

  }

  return size - dup;
}



int main() {

  int A []= {1 , 2, 3, 3};

  printf("unique items in list: %d", countUnique(A, sizeof(A)/ sizeof(int)));
  return 0;
}


// index
// size
// iter A
 // iter A
