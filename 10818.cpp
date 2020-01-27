#include<iostream>
using namespace std;
int main(void)
{
	int num,a,max,min;
	cin >> num;
	int* list = new int[num];
	for (int i = 0; i < num; i++)
	{
		cin >>	 a;
		list[i] = a;
	}
	max = list[0];
	min = list[0];
	for (int j = 0; j < num; j++)
	{
		if (max < list[j])
			max = list[j];
		if (min > list[j])
			min = list[j];
	}
	cout << min << " " << max;
}