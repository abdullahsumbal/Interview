#include <stdlib.h>
#include <stdio.h>

 int main(int argc, char const *argv[]) {
  char * string = "iamstupid";
  char string1 [] = "iamverystupid";

  // Const is a compile time constrait that the object can not be modified
  const int i = 5;
  // we cant do this. the becasue i is const.
  //int * p = &i;

  // p is not const. the data pointing to p is const
  const int * p = &i;

  // we can not do this
  //*p = 6;

  // But we can do this
  p++;

  // The p2 is const but the data is not cosnt
  int * const p2 = NULL;

  // integer and pointer is const
  const int * const p3 = NULL;

  const int a = 4;

  const_cast<int&>(a) = 9;

  return 0;
}
