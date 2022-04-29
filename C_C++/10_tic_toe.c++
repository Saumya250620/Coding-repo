#include <iostream>
using namespace std;

char matrix[3][3] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
void Draw()
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; i < 3; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    Draw();
    system("pause");
    return 0;
} 