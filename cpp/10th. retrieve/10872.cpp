//
// Created by gkrtj on 2020-02-01.
//
#include <iostream>
using namespace std;
int factorial(int num);
int main(void)
{
    int num;
    cin>>num;
    cout<<factorial(num)<<endl;
}
int factorial(int a)
{
    if(a > 1)
        return a * factorial(a-1);
    else if(a == 0)
        return 1;
    else
        return a;
}