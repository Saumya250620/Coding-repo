/*C++ program for Tabulated version */
#include <iostream>
using namespace std;

/* function for nth Fibonacci number */
int fib(int n){
    int f[n + 1];
    int i;
    f[0] = 0;
    f[1] = 1;

    for(i = 2; i <= n; i++){
        f[i] = f[i - 1] + f[i - 2];
    }
    return f[n];
}


// Driver mode
int main(){
    int n = 3;
    cout << "Fibonacci number is " << fib(n) << endl;
    return 0;
}