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

bool search(Node *root, int x){
    if(root == NULL)
        return false;
    if(root -> data == x)
        return true;
    else if(root -> data > x)
        return search(root -> left, x);
    else
        return search(root -> right, x);
}

int main(){
    Node *root = new Node(15);
    root -> left = new Node(5);
    root -> left -> left = new Node(3);
    root -> right = new Node(20);
    root -> right -> left = new Node(18);
    root -> right -> left -> left = new Node(16);
    root -> right -> right = new Node(80);
    int x = 17;

    if(search(root, x))
        cout << "Found";
    else
        cout << "Not Found";
}