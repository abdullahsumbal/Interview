#include <stdio.h>
#include<stdlib.h>

typedef struct Node{
  int val;
  struct Node * left, *right;
}node ;

node * newNode(int val){
  node* n = malloc(sizeof(node));
  n->val = val;
  n->left = NULL;
  n->right = NULL;

  return n;
}

// [ left, root, right ]
void inorder(node * n){
  if(n->left != NULL)
    inorder(n->left);
  printf("%d ,", n->val);
  if(n->right != NULL)
    inorder(n->right);

}

// [ left, right, visit ]
void postorder(node * n){

  if(n->left != NULL)
    postorder(n->left);
  if(n->right != NULL)
    postorder(n->right);

  printf("%d\n", n->val);

}

// [ visit, left, right ]
void preorder(node * n){
  printf("%d\n", n->val);
  if(n->left != NULL)
    postorder(n->left);
  if(n->right != NULL)
    postorder(n->right);

}

int max_kth(node * n, int k, int count){
  if (n == NULL){
    return 0;
  }
  if (count > k)
    return 0;

  int ans = max_kth(n->right, k, count);

  if(count >= k)
    return ans;

  ans += n->val;
  count ++;

  if(count >= k)
    return ans;

  return ans + max_kth(n->left, k, count);
}

node * insert(node * n, int val){
  if(n == NULL) return newNode(val);

  if(val < n->val){
    n->left = insert(n->left, val);
  }else{
    n->right = insert(n->right, val);
  }
  return n;
}

// A function to find k'th largest element in a given tree.
void kthLargestUtil(node *root, int k, int* c)
{
    // Base cases, the second condition is important to
    // avoid unnecessary recursive calls
    if (root == NULL || *c >= k)
        return;

    // Follow reverse inorder traversal so that the
    // largest element is visited first
    kthLargestUtil(root->right, k, c);

    // Increment count of visited nodes
    *c = *c +1;

    // If c becomes k now, then this is the k'th largest
    if (*c == k)
    {
      printf("%d\n", root->val);
        return;
    }

    // Recur for left subtree
    kthLargestUtil(root->left, k, c);
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

int  minNext(node * n){
  if(n->left == NULL){
    return n->val;
  }
  return minNext(n->left);
}

int maxheight(node *n){
    if(n == NULL){
      return 0;
    }
    int leftheight =+ (maxheight(n->left) + 1);
    int rightheight =+ (maxheight(n->right) + 1);

    int max = leftheight > rightheight? leftheight : rightheight;

    return max;

}

int pathLen(node * n, int val){
    if(n == NULL){
      return 0;
    }
    if(val < n->val){
      return pathLen(n->left, val) + 1;
    }else if (val > n->val){
      return pathLen(n->right, val)+1;
    }
    // found val
    else{
      return 1;
    }

}

int firstCommon(node * n, int val1, int val2){
    if(n == NULL){
      return 0;
    }
    if(val1 < n->val && val2 < n->val){
      return firstCommon(n->left, val1, val2) ;
    }else if (val1 > n->val && val2 > n->val){
      return firstCommon(n->right, val1, val2);
    }
    // found val
    else{
      return n->val;
    }

}


int main(int argc, char const *argv[]) {
  node * root = newNode(9);
  insert(root, 7);
  //printf("hello world");
  // /rintf("%d\n", root->left->val);
  insert(root, 8);
  insert(root, 2);
  insert(root, 10);
  insert(root, 1);
  int c = 0;
  int * p = &c;
  kthLargestUtil(root, 2, p);

  printf("%d\n", maxheight(root));
  printf("%d\n",pathLen(root, 9) );
  printf("%d\n",firstCommon(root, 8, 1) );
  return 0;
}
