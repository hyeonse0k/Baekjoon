//
// Created by gkrtj on 2020-01-29.
//
#include <iostream>
using namespace std;
bool han_num(int a);
int main(void)
{
    int num, count = 0;
    cin >> num;
    for(int i = 1; i <= num ; i++)
    {
        if(han_num(i))
            count++;
    }
    cout<<count<<endl;
}
bool han_num(int num)
{
    if(num < 100)
        return true;

    int a, b ,c;
    a = num / 100;
    b = num % 100 / 10;
    c = num % 10;
    if ((((a-b) == (b-c) || ((b-a) == (c-b)))))
        return true;
    else
        return false;
}
