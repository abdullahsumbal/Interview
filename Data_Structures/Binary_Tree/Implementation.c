#include <stdio.h>
#include <stdlib.h>


struct node
{
  int value;
  struct node *left;
  struct node *right;
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

/* A utility function to insert a new node with given value in BST */
struct node* insert(struct node* node, int value)
{
    /* If the tree is empty, return a new node */
    if (node == NULL) return newNode(value);

    /* Otherwise, recur down the tree */
    if (value < node->value)
        node->left  = insert(node->left, value);
    else if (value > node->value)
        node->right = insert(node->right, value);

    /* return the (unchanged) node pointer */
    return node;
}

int main(int argc, char const *argv[]) {
  struct node *root = newNode(1);
  insert(root, 19);
  insert(root, 15);
  printf("%d\n", root->right->left->value);
  return 0;
}


/*
Things I learned
1. I cant not initialize a variable in struct
2. Need to put ";" after struct
*/
