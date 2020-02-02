//
// Created by gkrtj on 2020-01-29.
//
#include <iostream>
using namespace std;
int main(void)
{
    char input[100];
    int index[26];
    fill_n(index, 26, -1);
    fill_n(input, 100, 0);
    cin>>input;
    for(int i = 0; i< 100; i++)
    {
        if(input[i] == '\0')
            break;
        if(index[input[i]-'a'] == -1)
            index[input[i] - 'a'] = i;
    }
    for(int i = 0 ; i < 26 ; i++)
    {
        cout<<index[i]<<" ";
    }
}
