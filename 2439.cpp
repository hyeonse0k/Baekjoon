#include <iostream>

using namespace std;
int main(void)
{
	int count;
	cin >> count;
	for (int i = count; i > 0; i--)
	{
		for (int j = i-1; j > 0; j--)
		{
			cout << " ";
		}
		for (int k = count - i; k >= 0; k --)
			cout << "*";
		cout << endl;
	}
}