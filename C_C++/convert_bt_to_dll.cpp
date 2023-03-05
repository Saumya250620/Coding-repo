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

void printlist(Node *head){
    Node *curr = head;
    while(curr != NULL){
        cout << curr -> key << " ";
        curr = curr -> right;
    }
    cout << endl;
}

int main(){
    Node *root = new Node(10);
    root -> left = new Node(5);
    root -> right = new Node(20);
    root -> right -> left = new Node(30);
    root -> right -> right = new Node(35);

    // Node *head = BTToDLL(root);
    printlist(root);
}