//
// Created by gkrtj on 2020-01-31.
//
#include <iostream>
#include <cmath>
using namespace std;
int main(void)
{
    double static_value, supply, sales;
    cin>>static_value>>supply>>sales;
    double count=0;
    if( supply >= sales) {
        cout << -1 << endl;
        return 0;
    }
    else {
        count = static_value / (sales - supply);
        printf("%.0lf", floor(count) + 1);
    }
}
