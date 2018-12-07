#include <stdio.h>
#include <stdlib.h>
// To execute C, please define "int main()"

typedef struct Node {

  int val;
  struct Node * left;
  struct Node * right;
} node;

node * newNode (int val){
  node * n = (node *)malloc(sizeof(node));
  n->val = val;
  n->left = NULL;
  n->right= NULL;
  return n;
}



node * insert (node * n, int val){

  if(n == NULL){
    return newNode(val);
  }
  if(n->val > val){
   n->left = insert(n->left, val);
  }else{
   n->right = insert(n->right, val);
  }

  return n;

}

int  minNext(node * n){
  if(n->left == NULL){
    return n->val;
  }
  return minNext(n->left);
}


node * deleteNode(node * n,int  val){
  if(n == NULL) return n;

  if(val < n->val){
    n->left = deleteNode(n->left, val);
  }else if (val > n->val){
    n->right = deleteNode(n->right, val);
  }
  // found node
  else{
    //case 1: no left child.
    if(n->left== NULL){
      return  n->right;
      //free(n);
      //return temp;
    }
    // case2: no right child
    if(n->right== NULL){
      return  n->left;
    }

    // have both child
    int newVal = minNext(n->right);
    n->val = newVal;
    n->right = deleteNode(n->right, newVal);
  }
  return n;
}

void inorder(node * n){

  if(n->left != NULL){
    inorder(n->left);
  }
  printf("%d\n",n->val);
  if(n->right != NULL){
   inorder(n->right);
  }
}
//
// node * deleteNode(node * n, int val){
//
//  if(n == NULL){
//   return n;
//  }
// if(val < n->val){
//     n->left = deleteNode(n->left, val);
//   }else if (val > n->val){
//     n->right = deleteNode(n->right, val);
//   }else{
//     // if it does not have left child
//     if(n->left == NULL){
//       n=  n->right;
//     }else if (n->right == NULL){
//
//       n =  n->left;
//     }
//     else{
//       int preVal = minNext(n,n->val);
//       n->val = preVal;
//       n->left = deleteNode(n->left, preVal);
//     }
//   }
// return n;
// }

int main() {

  node * root = newNode(5);
  insert(root, 6);
  insert(root, 7);

  inorder(root);
  root = deleteNode(root, 5);
  inorder(root);
  return 0;

}
