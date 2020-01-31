//
// Created by gkrtj on 2020-01-29.
//
#include <iostream>
using namespace std;
int main(void)
{
    int subject_num = 0;
    cin>>subject_num;
    float *score = new float[subject_num];
    float sum = 0, max = 0, mean;
    for(int i = 0; i < subject_num ; i++)
    {
        int a;
        cin >> a;
        if(a > max)
            max = a;
        score[i] = a;
    }
    for(int i = 0; i < subject_num ; i++)
    {
        score[i] = score[i] / max * 100;
        sum += score[i];
    }
    mean = sum / subject_num;
    cout<<fixed;
    cout.precision(2);
    cout<<mean<<endl;
}
