//
// Created by hyunseok on 2020-01-29.
//
#include <iostream>
using namespace std;
int main(void)
{
    int *num_1 = new int[100];
    int *num_2 = new int[100];
    int i = 0;
    while(1)
    {
        cin>>num_1[i]>>num_2[i];
        if(num_1[i] == 0 && num_2[i] == 0)
            break;
        i++;
    }
    for(int j = 0; j < i ; j++)
    {
        cout<<num_1[j] + num_2[j]<<endl;
    }
}
