#include <bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    Node *next;
    Node(int x){
        data = x;
        next = NULL;
    }
};

void printlist(Node *head)
{
    if(head == NULL) return;
    Node *p = head;
    do{
        cout << p-> data << " ";
        p = p -> next;
    }while(p != head);
}

Node *insertbegin(Node *head, int x){
    Node *temp = new Node(x);
    if(head == NULL)
        temp -> next = temp;
    else{
        Node *curr = head;
        while(curr -> next != head)
            curr = curr -> next;
        curr -> next = temp;
        temp -> next = head;
    }
    return temp;
}
int main(){
    Node *head = new Node(10);
    head -> next = new Node(20);
    head -> next -> next = new Node(30);
    head -> next -> next -> next= head;
    head = insertbegin(head, 15);
    printlist(head);
    return 0;
}