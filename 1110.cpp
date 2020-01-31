//
// Created by gkrtj on 2020-01-29.
//
#include <iostream>
using namespace std;
int main(void)
{
    int org_num;
    cin>>org_num;
    int old_num, new_num = 10000;
    int count = 0;
    old_num = org_num;
    while(org_num != new_num)
    {
        count++;
        new_num = (old_num % 10) * 10 + (old_num / 10 + old_num % 10) % 10;
        old_num = new_num;
    }
    cout<<count<<endl;
}

