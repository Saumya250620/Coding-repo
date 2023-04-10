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
    Node *temp = new Node(x);
    Node *parent = NULL, *curr = root;
    while(curr != NULL){
        parent = curr;
        if(curr -> data > x)
            curr = curr -> left;
        else if(curr -> data < x)
            curr = curr -> right;
        else 
            return root;
    }
    if(parent == NULL)
        return temp;
    if(parent -> data > x)
        parent ->left = temp;
    else 
        parent -> right = temp;
    return root;
}

void inorder(Node *root){
    if(root != NULL){
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