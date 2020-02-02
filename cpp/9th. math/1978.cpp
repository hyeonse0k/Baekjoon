//
// Created by gkrtj on 2020-01-31.
//
#include <iostream>
#include <cmath>
using namespace std;
bool check_prime(int a);
int main(void)
{
    int num;
    int prime_count = 0;
    cin>>num;
    int *array = new int[num];
    for(int i = 0; i < num; i++) {
        cin>>array[i];
        if(check_prime(array[i]))
            prime_count++;
    }
    cout<<prime_count<<endl;
}
bool check_prime(int a)
{
    if(a == 1)
        return false;
    for(int i = 2; i <= sqrt(a) ; i++)
    {
        if(a % i == 0)
            return false;
    }
    return true;
}