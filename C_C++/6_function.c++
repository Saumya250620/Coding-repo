#include <iostream>
#include <windows.h>
using namespace std;

int sum(int a, int b)
{
    cout<<"Function Sum is executing"<< endl;
    int c;
    c = a + b;
    return c;
}

void WelcomeMessange()
{
    cout<<"Welcome to our program!"<<endl;
}

void StartProgram(string filename)
{
    ShellExecute(NULL , "open",filename.c_str(),NULL,NULL,SW_SHOWNORMAL);
}
int main()
{
    WelcomeMessange();
    int x, y;
    cin >> x;
    cin >> y;
    cout << sum(x, y) << endl;
    StartProgram("mspaint");
    system("pause");
    return 0;
}