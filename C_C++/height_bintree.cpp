#include <bits/stdc++.h>
using namespace std;

struct Node{
    int key;
    Node *right;
    Node *left;
    Node(int k){
        key = k;
        right = left = NULL;
    }
};

int height(Node *root){
    if(root == NULL)
        return 0;
    else
        return(1 + max(height(root ->left), height(root -> right)));
}

int main(){
    Node *root = new Node(10);
    root -> left = new Node(20);
    root -> right = new Node(30);
    root -> right -> left = new Node(40);
    root -> right -> right = new Node(50);
    // root -> right -> right -> left = new Node(60);

    cout << height(root);
}