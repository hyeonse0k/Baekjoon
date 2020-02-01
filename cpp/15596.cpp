//
// Created by gkrtj on 2020-01-29.
//
#include <iostream>
#include <vector>
using namespace std;
long long sum(vector<int> &a)
{
    long long sum;
    for(int i = 0 ; i < a.size() ; i++)
    {
        sum +=a.at(i);
    }
    return sum;
}