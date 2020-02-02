//
// Created by gkrtj on 2020-02-01.
//
#include <iostream>
using namespace std;
int fibo(int num);
int main(void)
{
    int num;
    cin >> num;
    cout<<fibo(num)<<endl;
}
int fibo(int a)
{
    if(a == 0)
        return 0;
    if(a == 1)
        return 1;
    else
        return fibo(a - 1) + fibo(a - 2);
}