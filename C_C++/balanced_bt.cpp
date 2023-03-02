#include <bits/stdc++.h>
using namespace std;

struct Node{
    int key;
    Node *right;
    Node * left;
    Node(int k){
        key = k;
        right = left = NULL;
    }
};

int height(Node *root){
    if(root == NULL)
        return 0;
    else
        return(1 + max(height(root -> left), height(root -> right)));
}

bool isBalanced(Node *root){
    if(root == NULL)
        return true;
    int lh = height(root -> left);
    int rh = height(root -> right);
    return (abs(lh-rh)<= 1 && isBalanced(root -> left) && isBalanced(root -> right));
}

int main(){
    Node *root = new Node(3);
    root -> left = new Node(4);
    root -> right = new Node(8);
    root -> left -> left = new Node(5);
    root -> left -> right = new Node(9);
    root -> right -> right = new Node(7);
    root -> right -> right -> left = new Node(6);

    cout << isBalanced(root);
}