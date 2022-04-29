#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cout << "Enter first number: ";
    cin >> a;
    cout << "Enter second number: ";
    cin >> b;

    if (a > b)
    {
        cout << "Variable A is greater than variable B." << endl;
        cout << "Value of a is " << a << ". Value of b is " << b << endl;
    }
    else if(a == -1 || b==-1)
    {
        return 0;
    }
    else if (a == b)
    {
        cout <<"Value of A is the same like the value of B." <<endl;
        cout << "A is "<< a << endl;
        cout << "B is "<< b <<endl;
    }
    else
    {
        cout << "Variable B is greater than variable A." << endl;
        cout << "Value of a is " << a << ". Value of b is " << b << endl;
    }
    system("pause");
    return 0;
}