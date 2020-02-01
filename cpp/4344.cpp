#include <iostream>
using namespace std;
int main() {
    int test_num;
    cin >> test_num;
    for(int i = 0; i < test_num; i++)
    {
        int stu_num;
        cin >> stu_num;
        int score_sum = 0;
        int over_count = 0;
        int * score_list = new int[1000];
        double avg, over_ratio;
        for (int j = 0; j < stu_num ; j++)
        {
            cin >> score_list[j];
            score_sum += score_list[j];
        }
        avg = score_sum / stu_num;
        for(int k = 0 ; k < stu_num; k++)
        {
            if(score_list[k] > avg)
                over_count++;
        }
        over_ratio = double(over_count) / stu_num * 100;
        printf("%.3f%%\n", over_ratio);
    }
}
