#include <stdio.h>
#include <stdlib.h>



struct node {
  int value;
struct   node * next;
struct   node * previous;
};


struct node * newNode(int value){
  struct node * root = malloc(sizeof(struct node));
  root->value = value;
  root->next = NULL;
  root->previous = NULL;
  return root;
};

int main(int argc, char const *argv[]) {

  struct node * item =  newNode(2);


  return 0;
}
