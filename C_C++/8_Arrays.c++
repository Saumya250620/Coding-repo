#include <iostream>
#include <time.h>
using namespace std;

int main()
{
    int b[5]={20,3,4,6,7};
    for(int i=0;i<5;i++)
    {
        cout<<"Enter number "<<i<<":";
        cin>>b[i];
    }
    for(int i=0;i<5;i++)
    {
        cout << b[i] << endl;
    }
    system("pause");
    return 0; 
}