#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node(int x)
    {
        data = x;
        next = NULL;
    }
};

void printlist(Node *head)
{
    if(head == NULL)
        return;
    
    cout << (head -> data) << " ";
    printlist(head->next);
}
Node *insertBegin(Node *head, int x)
{
    Node *temp = new Node(x);
    temp -> next = head;
    return temp;
};
int main()
{
    Node *head = NULL;
    head = insertBegin(head, 30);
    head = insertBegin(head, 20);
    head = insertBegin(head, 10);
    printlist(head);
    return 0;
}
