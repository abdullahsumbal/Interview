#include <stdio.h>
#include <stdlib.h>


struct node
{
  int value;
  struct Node *left;
  struct Node *right;
};

struct node * newNode(int value)
{
  struct node * node = malloc(sizeof(struct node));
  node->value = value;

  //initialize left and right child
  node->left = NULL;
  node->right = NULL;
  return node;
};



int main(int argc, char const *argv[]) {
  /* code */
  return 0;
}


/*
Things I learned
1. I cant not initialize a variable in struct
2. Need to put ";" after struct
*/
