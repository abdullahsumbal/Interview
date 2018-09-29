#include <iostream>

using namespace std;


struct node {
  node * left;
  node * right;
  int value;
};

class BST{
public:
  node * root = new node;
  void insert(int);
  BST(int value){
     root->value = value;
     root->left = NULL;
     root->right = NULL;
  }
private:
  node * addRecursive(node *, int);
};

int main(){
  BST bst(10);
  bst.insert(13);
  bst.insert(3);
  bst.insert(12);
  bst.insert(5);

  cout << bst.root->right->value << endl;
}

void BST::insert(int value){
  BST::addRecursive(root, value);
}

node * BST::addRecursive(node * root, int value){

  if(root == NULL){
    node * n = new node;
    n->left = NULL;
    n->right = NULL;
    n->value = value;
    return n;
  }else if(root->value < value){
    root->right = addRecursive(root->right, value);
  }else if(root->value > value){
    root->left = addRecursive(root->left, value);
  }else{
    return root;
  }
  return root;

}
