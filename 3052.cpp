//
// Created by gkrtj on 2020-01-29.
//
#include <iostream>
using namespace std;
int main(void)
{
    int num[10];
    int check[42] = {0};
    int count = 0;
    for(int i = 0; i < 10; i++)
    {
        int a;
        cin>>a;
        num[i] = a % 42;
    }
    for(int j = 0; j < 10; j++)
    {
        if(check[num[j]] == 0)
        {
            count++;
            check[num[j]] = 1;
        }
    }
    cout<<count<<endl;
}

