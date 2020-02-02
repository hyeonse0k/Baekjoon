//
// Created by gkrtj on 2020-01-31.
//
#include <iostream>
#include <string>
using namespace std;
int find_time(char a);
int main(void)
{
    string input;
    getline(cin, input);
    int time = 0;
    for(int i = 0 ; i < input.size() ; i++)
    {
        time += find_time(input[i]);
    }
    cout<<time<<endl;
}
int find_time(char a)
{
    if(a-'W' >= 0)
        return 10;
    else if(a-'T' >= 0)
        return 9;
    else if(a-'P' >= 0)
        return 8;
    else if(a-'M' >= 0)
        return 7;
    else if(a-'J' >= 0)
        return 6;
    else if(a-'G' >= 0)
        return 5;
    else if(a-'D' >= 0)
        return 4;
    else
        return 3;
}