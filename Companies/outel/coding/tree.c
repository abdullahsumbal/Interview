#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
  int val;
  struct Node * left;
  struct Node * right;
} node;

node * newNode(int val){
  node* n = (node *)malloc(sizeof(node));
  n->val = val;
  n->left =  NULL;
  n->right = NULL;
}

node * insert(node* n, int val){
  if(n == NULL){
    return newNode(val);
  }

  if(n->val >= val){
    n->left = insert(n->left, val);
  }else{
    n->right = insert(n->right, val);
  }
  return n;
}

void inorder(node * n){
  if(n->left != NULL)
    inorder(n->left);
  printf("%d\n", n->val);
  if(n->right != NULL){
    inorder(n->right);
  }
}

int maxheight(node * n){

  if(n == NULL){
    return 0;
  }

  int left = maxheight(n->left) + 1;
  int right = maxheight(n->right) + 1;

  if(left > right){
    return left;
  }else{
    return right;
  }
}

int kth_max(node * n, int k){
  static int count = 0;
  if(n == NULL){
    return 0;
  }
  if(count == k){
    return n->val;
  }
  int ans = kth_max(n->right, k);
  count++;
  if(count == k){
    return n->val;
  }
  return (ans + kth_max(n->left, k));
}



int main(int argc, char const *argv[]) {

  node * root = newNode(12);
  insert(root, 10);
  insert(root, 13);
  insert(root, 3);
  insert(root, 20);
  insert(root, 16);
  insert(root, 8);

  inorder(root);

  printf("%d\n",kth_max(root, 3) );

  //printf("%d\n",maxheight(root) );


  return 0;
}
