//
// Created by gkrtj on 2020-01-31.
//
#include <iostream>
#include <string>
using namespace std;
int main(void)
{
    string words;
    int word_count = 0;
    getline(cin, words);
    int i;
    for(i = 0 ; i < words.size() ; i++)
    {
        if( words[i] != '\n' && i != 0 && words[i] == ' ' && words[i+1] != ' ' && words[i+1] != 0)
            word_count++;
    }
    if(words.size() == 0 || (words.size() == 1 && words[0] == ' '))
        word_count--;
    cout<<word_count+1<<endl;
}