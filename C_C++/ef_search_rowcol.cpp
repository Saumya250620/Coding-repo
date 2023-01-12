#include <bits/stdc++.h>
using namespace std;

const int r = 4, c = 4;

void search(int arr[r][c], int x)
{
    int i = 0, j = c-1;

    while(i < r && j >=0)
    {
        if(arr[i][j] == x)
        {
            cout << "Found at (" << i << ", " << j << ")";
            return;
        }
        else if(arr[i][j] > x)
            j--;
        else
            i++;
    }
}
int main()
{
    int arr[r][c] = {{10,20,30,40},
                    {15,25,35,45},
                    {27,29,37,48},
                    {32,33,39,50}};
    
    int x = 29;

    search(arr,x);

    return 0;
}