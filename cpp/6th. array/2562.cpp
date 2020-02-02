#include <iostream>
using namespace std;
int main(void)
{
	int max, num, max_i;
	max = 0;
	int num_list[9];
	for (int i = 0; i < 9; i++)
	{
		cin >> num;
		num_list[i] = num;
		if (num > max)
		{
			max = num;
			max_i = i+1;
		}
	}
	cout << max << endl;
	cout << max_i << endl;
}