#include <bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    Node *left;
    Node *right;
    Node(int k){
        data = k;
        left = right = NULL;
    }
};

Node *insert(Node *root, int x){
    if(root == NULL)
        return new Node(x);
    if(root -> data > x)
        root -> left = insert(root-> left, x);
    else //if(root -> data < x)
        root -> right = insert(root -> right, x);
    return root;
}

void inorder(Node *root){
    if(root!=NULL){
        inorder(root -> left);
        cout << root -> data << " ";
        inorder(root -> right);
    }
}

int main(){
    Node *root = new Node(10);
    root -> left = new Node(5);
    root -> right = new Node(15);
    root -> right -> left = new Node(12);
    root -> right -> right = new Node(18);
    int x = 20;

    root = insert(root, x);
    inorder(root);
}