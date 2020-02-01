//
// Created by gkrtj on 2020-01-29.
//
#include <iostream>
using namespace std;
int main(void)
{
    int num, sum = 0;
    cin>>num;
    char value[100];
    cin>>value;
    for(int i = 0 ; i < num; i++)
    {
        sum += value[i] - '0';
    }
    cout<<sum<<endl;
}
