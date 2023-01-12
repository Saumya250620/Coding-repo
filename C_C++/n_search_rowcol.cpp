#include <bits/stdc++.h>
using namespace std;

const int r = 4, c = 4;

void search(int arr[r][c], int x)
{
    for(int i = 0; i < r; i++)
    {
        for(int j = 0; j < c; j++)
        {
            if(arr[i][j] == x)
            {
                cout << "Found at (" << i << ", " << j << ")";
                return;
            }
        }
    }
    cout << "Not Found";
}
int main()
{
    int arr[][c] = {{10,20,30,40},
                    {15,25,35,45},
                    {27,29,35,45},
                    {32,33,39,50}};

    int x = 29;

    search(arr, x);

    return 0;
}