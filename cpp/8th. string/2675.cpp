//
// Created by gkrtj on 2020-01-29.
//
#include <iostream>
using namespace std;
int main(void)
{
    int test_count;
    cin>>test_count;
    for(int i = 0; i < test_count ; i++)
    {
        int loop = 0;
        char string[21];
        fill_n(string, 21, 0);
        cin>>loop>>string;

        for(int j = 0 ; j < 21 ; j++)
        {
            if(string[j] == '\0')
            {
                cout<<endl;
                break;
            }
            for(int k = 0; k < loop; k++) {
                cout << string[j];
            }
        }
    }
}
