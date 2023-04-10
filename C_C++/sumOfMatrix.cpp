// C++ code to implement the approach
#include <bits/stdc++.h>
using namespace std;

int sumOfMatrix(int N, int M, vector<vector<int>> mat){
    int sum = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            sum += mat[i][j];
        }
    }
    return sum;
}

int main(){
    vector<vector<int>> mat = {{4, 5, 3, 2}, {9, 5, 6, 2}, {1, 5, 3, 5}};

    int N = mat.size();
    int M = mat[0].size();

    // Function call
    cout << sumOfMatrix(N, M, mat) << endl;

    return 0;
}