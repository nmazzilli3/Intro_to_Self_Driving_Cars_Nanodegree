//TODO: Write a function that receives two integer matrices and outputs
// the sum of the two matrices. Then in your main() function, input a few
// examples to check your solution. Output the results of your function to 
// cout. You could even write a separate function that prints an arbitrarily 
// sized matric to cout.

// TODO: Include the iostream and vector libraries
#include <iostream>
#include <vector>
using namespace std;
// TODO: Use the standard namespace
vector < vector <int> > matrix_add(vector < vector <int> > matrix1,vector < vector <int> >matrix2)
{
    vector < vector <int> > matrix3 (matrix1.size(), vector <int> (matrix1[0].size()));
    for (int row = 0; row < matrix1.size(); row++) 
    {
        for (int column = 0; column < matrix1[0].size(); column++) 
        {
            matrix3[row][column] = matrix1[row][column]+matrix2[row][column];
        }  
    }
        
    return matrix3;
    
}
// TODO: Write a main function
int main() 
{
// TODO: Inside the main function, do the following:
vector < vector <int> > matrix1 (5, vector <int> (3, 2));
vector < vector <int> > matrix2 (5, vector <int> (3, 2));
vector < vector <int> > matrix3 (5, vector <int> (3));

matrix3 = matrix_add(matrix1,matrix2);

for (int row = 0; row < matrix3.size(); row++) {
        for (int column = 0; column < matrix3[0].size(); column++) {
            cout << matrix3[row][column] << " ";
        }
        cout << endl;
}

return 0;
}