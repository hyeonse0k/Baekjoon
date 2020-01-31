#include <iostream>
using namespace std;
int main(void)
{
    char string[1000001];
    int alphabet[26];
    int max = 0, max_count = 0, max_index = 0;
    fill_n(alphabet, 26, 0);
    fill_n(string, 1000001, 0);
    cin>> string;
    int i = 0;
    while(string[i] != '\0')
    {
        if(string[i] >= 'A' && string[i] <= 'Z')
            alphabet[string[i] - 'A']++;
        else
            alphabet[string[i] - 'a']++;
        i++;
    }
    for(int j = 0; j < 26; j++) {
        if (alphabet[j] > max) {
            max = alphabet[j];
            max_index = j;
        }
    }
    for(int k = 0; k < 27; k++)
    {
        if(alphabet[k] == max)
            max_count++;
    }
    if(max_count != 1)
        cout<<"?"<<endl;
    else
        cout<<(char)(max_index+'A')<<endl;
}